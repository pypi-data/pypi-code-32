# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


schema = {'children': {'required': False, 'anyof': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}, {'type': 'component'}, {'allowed': [None], 'type': ('string', 'number'), 'nullable': True}, {'type': 'list', 'schema': {'anyof': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}, {'type': 'component'}, {'allowed': [None], 'type': ('string', 'number'), 'nullable': True}], 'nullable': True}}], 'nullable': True}}

class Form(Component):
    """A Form component.


Keyword arguments:
- children (string | number | boolean | dash component | a value equal to: null | list; optional): The children of this component
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- n_clicks (number; optional): An integer that represents the number of times
that this element has been clicked on.
- n_clicks_timestamp (number; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- role (string; optional): The ARIA role attribute
- data-* (string; optional): A wildcard data attribute
- aria-* (string; optional): A wildcard aria attribute
- accept (string; optional): List of types the server accepts, typically a file type.
- acceptCharset (string; optional): List of supported charsets.
- action (string; optional): The URI of a program that processes the information submitted via the form.
- autoComplete (string; optional): Indicates whether controls in this form can by default have their values automatically completed by the browser.
- encType (string; optional): Defines the content type of the form date when the method is POST.
- method (string; optional): Defines which HTTP method to use when submitting the form. Can be GET (default) or POST.
- name (string; optional): Name of the element. For example used by the server to identify the fields in form submits.
- noValidate (string; optional): This attribute indicates that the form shouldn't be validated when submitted.
- target (string; optional)
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- className (string; optional): Often used with CSS to style elements with common properties.
- contentEditable (string; optional): Indicates whether the element's content is editable.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- draggable (string; optional): Defines whether the element can be dragged.
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- lang (string; optional): Defines the language used in the element.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.

Available events: 'click'"""
    _schema = schema
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, accept=Component.UNDEFINED, acceptCharset=Component.UNDEFINED, action=Component.UNDEFINED, autoComplete=Component.UNDEFINED, encType=Component.UNDEFINED, method=Component.UNDEFINED, name=Component.UNDEFINED, noValidate=Component.UNDEFINED, target=Component.UNDEFINED, accessKey=Component.UNDEFINED, className=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, lang=Component.UNDEFINED, spellCheck=Component.UNDEFINED, style=Component.UNDEFINED, tabIndex=Component.UNDEFINED, title=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'accept', 'acceptCharset', 'action', 'autoComplete', 'encType', 'method', 'name', 'noValidate', 'target', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title']
        self._type = 'Form'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = ['click']
        self.available_properties = ['children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'accept', 'acceptCharset', 'action', 'autoComplete', 'encType', 'method', 'name', 'noValidate', 'target', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args}
        args.pop('children', None)
        super(Form, self).__init__(children=children, **args)
    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Form(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Form(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
