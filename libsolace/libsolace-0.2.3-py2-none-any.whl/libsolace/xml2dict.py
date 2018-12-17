#!/usr/bin/env python
"Makes working with XML feel like you are working with JSON"

from xml.parsers import expat
from xml.sax.saxutils import XMLGenerator
from xml.sax.xmlreader import AttributesImpl
try: # pragma no cover
    from cStringIO import StringIO
except ImportError: # pragma no cover
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
# try: # pragma no cover
#     from collections import OrderedDict
# except ImportError: # pragma no cover
OrderedDict = dict

try: # pragma no cover
    _basestring = basestring
except NameError: # pragma no cover
    _basestring = str
try: # pragma no cover
    _unicode = unicode
except NameError: # pragma no cover
    _unicode = str

__author__ = 'Martin Blech'
__version__ = '0.3'
__license__ = 'MIT'

class ParsingInterrupted(Exception): pass

class _DictSAXHandler(object):
    def __init__(self,
                 item_depth=0,
                 item_callback=lambda *args: True,
                 xml_attribs=True,
                 attr_prefix='@',
                 cdata_key='#text',
                 force_cdata=False,
                 cdata_separator='',
                 postprocessor=None):
        self.path = []
        self.stack = []
        self.data = None
        self.item = None
        self.item_depth = item_depth
        self.xml_attribs = xml_attribs
        self.item_callback = item_callback
        self.attr_prefix = attr_prefix;
        self.cdata_key = cdata_key
        self.force_cdata = force_cdata
        self.cdata_separator = cdata_separator
        self.postprocessor = postprocessor

    def startElement(self, name, attrs):
        self.path.append((name, attrs or None))
        if len(self.path) > self.item_depth:
            self.stack.append((self.item, self.data))
            attrs = OrderedDict((self.attr_prefix+key, value)
                    for (key, value) in attrs.items())
            self.item = self.xml_attribs and attrs or None
            self.data = None

    def endElement(self, name):
        if len(self.path) == self.item_depth:
            item = self.item
            if item is None:
                item = self.data
            should_continue = self.item_callback(self.path, item)
            if not should_continue:
                raise ParsingInterrupted()
        if len(self.stack):
            item, data = self.item, self.data
            self.item, self.data = self.stack.pop()
            if data and self.force_cdata and item is None:
                item = OrderedDict()
            if item is not None:
                if data:
                    item[self.cdata_key] = data
                self.push_data(name, item)
            else:
                self.push_data(name, data)
        else:
            self.item = self.data = None
        self.path.pop()

    def characters(self, data):
        if data.strip():
            if not self.data:
                self.data = data
            else:
                self.data += self.cdata_separator + data

    def push_data(self, key, data):
        if self.postprocessor is not None:
            key, data = self.postprocessor(self.path, key, data)
        if self.item is None:
            self.item = OrderedDict()
        try:
            value = self.item[key]
            if isinstance(value, list):
                value.append(data)
            else:
                self.item[key] = [value, data]
        except KeyError:
            self.item[key] = data

def parse(xml_input, *args, **kwargs):
    """Parse the given XML input and convert it into a dictionary.

    `xml_input` can either be a `string` or a file-like object.

    If `xml_attribs` is `True`, element attributes are put in the dictionary
    among regular child elements, using `@` as a prefix to avoid collisions. If
    set to `False`, they are just ignored.

    Simple example::

        >>> doc = xmltodict.parse(\"\"\"
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>
        ... \"\"\")
        >>> doc['a']['@prop']
        u'x'
        >>> doc['a']['b']
        [u'1', u'2']

    If `item_depth` is `0`, the function returns a dictionary for the root
    element (default behavior). Otherwise, it calls `item_callback` every time
    an item at the specified depth is found and returns `None` in the end
    (streaming mode).

    The callback function receives two parameters: the `path` from the document
    root to the item (name-attribs pairs), and the `item` (dict). If the
    callback's return value is false-ish, parsing will be stopped with the
    :class:`ParsingInterrupted` exception.

    Streaming example::

        >>> def handle(path, item):
        ...     print 'path:%s item:%s' % (path, item)
        ...     return True
        ...
        >>> xmltodict.parse(\"\"\"
        ... <a prop="x">
        ...   <b>1</b>
        ...   <b>2</b>
        ... </a>\"\"\", item_depth=2, item_callback=handle)
        path:[(u'a', {u'prop': u'x'}), (u'b', None)] item:1
        path:[(u'a', {u'prop': u'x'}), (u'b', None)] item:2

    The optional argument `postprocessor` is a function that takes `path`, `key`
    and `value` as positional arguments and returns a new `(key, value)` pair
    where both `key` and `value` may have changed. Usage example::

        >>> def postprocessor(path, key, value):
        ...     try:
        ...         return key + ':int', int(value)
        ...     except (ValueError, TypeError):
        ...         return key, value
        >>> xmltodict.parse('<a><b>1</b><b>2</b><b>x</b></a>',
        ...                 postprocessor=postprocessor)
        OrderedDict([(u'a', OrderedDict([(u'b:int', [1, 2]), (u'b', u'x')]))])

    """
    handler = _DictSAXHandler(*args, **kwargs)
    parser = expat.ParserCreate()
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.characters
    if hasattr(xml_input, 'read'):
        parser.ParseFile(xml_input)
    else:
        parser.Parse(xml_input, True)
    return handler.item

def _emit(key, value, content_handler,
         attr_prefix='@',
         cdata_key='#text',
         root=True):
    if not isinstance(value, (list, tuple)):
        value = [value]
    if root and len(value) > 1:
        raise ValueError('document with multiple roots')
    for v in value:
        if v is None:
            v = OrderedDict()
        elif not isinstance(v, dict):
            v = _unicode(v)
        if isinstance(v, _basestring):
            v = OrderedDict(((cdata_key, v),))
        cdata = None
        attrs = OrderedDict()
        children = []
        for ik, iv in v.items():
            if ik == cdata_key:
                cdata = iv
                continue
            if ik.startswith(attr_prefix):
                attrs[ik[len(attr_prefix):]] = iv
                continue
            children.append((ik, iv))
        content_handler.startElement(key, AttributesImpl(attrs))
        for child_key, child_value in children:
            _emit(child_key, child_value, content_handler,
                 attr_prefix, cdata_key, False)
        if cdata is not None:
            content_handler.characters(cdata)
        content_handler.endElement(key)


def unparse(item, output=None, encoding='utf-8', **kwargs):
    ((key, value),) = item.items()
    must_return = False
    if output == None:
        output = StringIO()
        must_return = True
    content_handler = XMLGenerator(output, encoding)
    content_handler.startDocument()
    _emit(key, value, content_handler, **kwargs)
    content_handler.endDocument()
    if must_return:
        value = output.getvalue()
        try: # pragma no cover
            value = value.decode(encoding)
        except AttributeError: # pragma no cover
            pass
        return value

if __name__ == '__main__': # pragma: no cover
    import sys
    import marshal

    (item_depth,) = sys.argv[1:]
    item_depth = int(item_depth)

    def handle_item(path, item):
        marshal.dump((path, item), sys.stdout)
        return True

    try:
        root = parse(sys.stdin,
                item_depth=item_depth,
                item_callback=handle_item)
        if item_depth == 0:
            handle_item([], root)
    except KeyboardInterrupt:
        pass
