from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from abc import ABCMeta, abstractmethod
import webbrowser
from clarus.models import ApiResponse
import clarus
from clarusui import utils
from premailer import Premailer
from lxml import html

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
env = Environment(
    loader=FileSystemLoader(THIS_DIR),
    autoescape=select_autoescape(['html', 'xml'])
)

layout_template = env.get_template('layout.html')
header_template = env.get_template('header.html')
anchor_template = env.get_template('anchor.html')
popover_template = env.get_template('popover.html')
statsgrid_template = env.get_template('statsgrid.html')

ASSIGNED_IDS = {}
def create_element_id(element):
    elementClass = type(element).__name__
    if ASSIGNED_IDS.get(elementClass) is None:
        ASSIGNED_IDS[elementClass] = 0
        
    elementIdx = ASSIGNED_IDS.get(elementClass)
    newId = str(elementClass)+'_'+str(elementIdx)
    ASSIGNED_IDS[elementClass] = elementIdx + 1
    return newId
            
class Element(object):
    
    __metaclass__ = ABCMeta
    def __init__(self, response, **options):
        self.id = create_element_id(self)
        self.response = response
        self._set_drilldown(options)
        self._set_realtime(options)
        self.set_css_class(options.pop('cssClass', ''))
        self.set_size(options.pop('size', None))
        self.customCss = {}
        self.set_custom_css(options.pop('customCss', None))
        self.set_height(options.pop('height', None))
        if options.get('bgcolour') is not None:
            self.add_custom_css({'background-color':options.get('bgcolour')})
        self.options = dict(options)
        self.set_header(options.pop('header',''))
    
    def get_id(self):
        return self.id
    
    def _set_realtime(self, options):
        self._realtimeGridId = options.pop('realtimeGridId', None)
    
    def listens_to_realtime(self, gridId):
        self._realtimeGridId = gridId
        
    def _set_drilldown(self, options):
        self._drilldownLink = None
        gridId = self._get_drilldown_grid_id(options)
        if gridId is not None:
            drilldownTitle = self._get_drilldown_title(options)
            self._drilldownLink = 'RiskRequest:DV01:gridId='+str(gridId)+';_breadcrumb=true;_title='+drilldownTitle
                
    def _get_drilldown_grid_id(self, options):
        gridId = options.pop('drilldownGridId', None)
        if gridId is None:
            gridId = self.get_grid_id()
        return gridId
    
    def get_grid_id(self):
        if isinstance(self.response, ApiResponse):
            return self.response.stats.get('GridId')
    
    def _get_drilldown_title(self, options):
        title = options.pop('drilldownTitle', None)
        if title is None:
            title = options.get('title', None)
        if title is None:
            title = 'Drilldown'
        return title            
                   
    def _get_rgbcolour(self, colour):
        return colour
    
    def __str__(self):
        return self.toHTML()

    @abstractmethod
    def toDiv(self):
        pass
    
    def toFinalElement(self):
        finalHtml = None
        if self._drilldownLink is None:
            finalHtml = self.toDiv()
        else :
            finalHtml = anchor_template.render(content=self.toDiv(), link=self._drilldownLink)
        return finalHtml

        
    def _build_rt_response(self, finalHtml):
        result = {}
        resultMeta = {}
        resultAttribs = {}
        result['resultData'] = finalHtml
        resultMeta['gridId'] = self._realtimeGridId
        resultAttribs['isGrid'] = True
        resultAttribs['subscriptions'] = [{'type':'Grid', 'ref':self._realtimeGridId}]
        result['resultMeta'] = resultMeta
        result['resultAttribs'] = resultAttribs
        return result       
        
    def toFile(self):
        tempFileName = 'temp-element.html'
        with open(tempFileName, 'w') as f:
            f.write(self.toHTML())
                    
        url = 'file://' + os.path.abspath(tempFileName)
        webbrowser.open(url)
        return url
            
  
    def toHTML(self, event=None):
        ASSIGNED_IDS.clear()
        finalHtml = None
        if event is not None and clarus.get_output_type(event) is not None and (clarus.get_output_type(event) == 'email' or clarus.get_output_type(event) == 'mail'):
            finalHtml = self.toInlinedHTML()
        else:
            finalHtml = self.toStandardHTML()
    
        if self._realtimeGridId is None or event is None or clarus.is_gui_call(event)==False:
            return finalHtml
        else:
            return self._build_rt_response(finalHtml)
    
    def toStandardHTML(self):
        self.add_custom_css({'min-height':'100vh'}) #should be the final step so should at least fill viewpoet
        base = env.get_template('base_content.html')
        return base.render(content=self.toDiv())
    
    def toInlinedHTML(self):
        self.add_custom_css({'font-size':'13px', 'max-width':'800px'})
        htmlOut = self.toStandardHTML()
        htmlOut = htmlOut.replace('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">', '')
        converter = Premailer(htmlOut, disable_leftover_css=True, 
                              keep_style_tags=False,
                              preserve_inline_attachments=False,
                              remove_classes=True,
                              disable_validation=True,
                              cssutils_logging_level='CRITICAL')
        dirtyHtml = converter.transform(pretty_print=False)
        doc = html.fromstring(dirtyHtml)
        for el in doc.cssselect('head'):
            el.drop_tree()
        for el in doc.cssselect('script'):
            el.drop_tree()
        result = html.tostring(doc, encoding = 'unicode')
        
        return result
   
    def toCSV(self):
        return self.response.text
        
    def set_css_class(self, cssClass):
        if (cssClass is not None):
            self.cssClass = cssClass
        else:
            self.cssClass = ''
    
    def add_css_class(self, cssClass):
        self.cssClass = self.cssClass + ' ' + cssClass
        
    def set_flash_colour(self, flashColour):
        if flashColour is not None:
            self.add_css_class('animated pulse')
            self.add_custom_css({'--flash-colour':flashColour})
            
    def set_custom_css(self, customCss):
        if (customCss is not None):
            self.customCss = customCss
    
    def add_custom_css(self, customCss):
        for key in customCss:
            self.customCss[key] = customCss.get(key)
            
    def _get_custom_css(self):
        if not self.customCss:
            return ''
        else:
            css = 'style="'
            for key in self.customCss:
                css = css + key + ':' + self.customCss.get(key) + ';'
            css = css + '"' 
            return css
    
    def _get_filtered_custom_css(self, filter):
        if not self.customCss:
            return ''
        
        if filter is None:
            return self._get_custom_css()
        
        if not isinstance(filter, list):
            filter = filter.split(',')
        hasValue = False
        css = 'style="'
        for key in self.customCss:
            if key in filter:
                css = css + key + ':' + self.customCss.get(key) + ';'
                hasValue = True
        css = css + '"'
        
        if hasValue:
            return css 
        return ''
                
    def set_bgcolour(self, colour):
        if colour is not None:
            self.add_custom_css({'background-color':colour})

    def set_size(self, size):
        if size is not None:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size > 12 or size < 1:
                raise ValueError("size must be 1 <= x <= 12 when specified")
        self.size = size
        
    def set_height(self, height):
        if height is not None:
            self.add_custom_css({'overflow-y':'auto', 'max-height':height})
            
    def _set_style(self, style):
        if 'background-color' not in self.customCss:
            self.set_bgcolour(style.getForegroundColour())
        if 'border-color' not in self.customCss:
            self.add_custom_css({"border-color":style.getBorderColour()})
            self.add_custom_css({"border-style":'solid'})
            self.add_custom_css({"border-width":'1px'})
        if 'font-family' not in self.customCss and 'color' not in self.customCss:
            self.set_font(style)
    
    def set_font(self, style):
        if style is not None:
            self.add_custom_css({"color":style.getFontColour()})
            self.add_custom_css({'font-family':style.getFontFamily()})
    
    def set_header(self, header):
        self._header = header
        
    def _get_header(self):
        return self._header       

class Dashboard(Element):
    def __init__(self, *childElements, **options):
        super(Dashboard, self).__init__(None,**options)
        self._stats = options.pop('stats', None)
        self.displayHeader = options.pop('displayHeader', bool(self._get_header()))
        self._set_child_elements(childElements)
        self.uniformColumnSize = options.pop('uniformColumnSize', False)
        self._finalise_column_sizing()        
        style = options.pop('style', None)
        if style is not None:
            self._set_style(style)
        
    
    def _set_style(self, style):
        if 'background-color' not in self.customCss:
            self.set_bgcolour(style.getBackgroundColour())
        if self.displayHeader == True:
            if 'background-color' not in self._header_element.customCss:
                self._header_element.set_bgcolour(style.getBackgroundColour())
        for elements in self.childElements:
            for element in elements:
                element._set_style(style)
             
    def _set_child_elements(self, childElements):
        self.childElements = []
        
        headerRow = []
        
        if self._stats is not None:
            statsPop = StatPopover(self._stats)
            headerRow.append(statsPop)
        
        if self.displayHeader == True:
            headerRow.insert(0, self._create_header_element())
        
        if len(headerRow) > 0:
            self.childElements.append(headerRow)
        
        for element in childElements:
            if not isinstance(element, list):
                self.childElements.append([element])
            else:
                self.childElements.append(element)
        
    def _finalise_column_sizing(self):
        if self.uniformColumnSize == True:
            self._uniform_column_size()
        else:
            self._auto_column_size()
        
    def _auto_column_size(self):
        for elements in self.childElements:
            holder = []
            unsizedElementCount = 0
            unpecifiedSizeRemaining = 12
    
            for element in elements:
                if element.size is None:
                    unsizedElementCount += 1
                else:
                    unpecifiedSizeRemaining = unpecifiedSizeRemaining - element.size
                holder.append(element)
            if unpecifiedSizeRemaining < 0:
                raise ValueError("specified sizes must total to <= 12")
    
            if (unsizedElementCount > 0):
                unspecifiedElementSize = int(unpecifiedSizeRemaining/unsizedElementCount)
                for i in holder:
                    if i.size is None:
                        i.size = unspecifiedElementSize
    
    def _uniform_column_size(self):
        maxNoOfColumns = 1
        for elements in self.childElements:
            if len(elements) > maxNoOfColumns:
                maxNoOfColumns = len(elements)
                
        for elements in self.childElements:
            for element in elements:
                element.size = int(12/maxNoOfColumns)
    
    def _create_header_element(self):
        header = Header(header=self._get_header())
        header.add_custom_css({'border-bottom-style':'solid', 'border-bottom-width':'1px', 'border-color':'#434857'})
        self._header_element = header
        return self._header_element
               
    def toDiv(self):
        return layout_template.render(dashboard=self)
    
class Grid(Dashboard):
    def __init__(self, *childElements, **options):
        self.columns = options.pop('columns', 2)
        laidOutChildren = self._layout_children(*childElements)
        super(self.__class__, self).__init__(uniformColumnSize=True,*laidOutChildren,**options)
        
    def _layout_children(self, childElements):
        chunks = self._chunk(childElements, self.columns)
        return list(chunks)
    
    def _chunk(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]  
            
class Header(Element):
    def __init__(self, **options):
        super(self.__class__, self).__init__(None, **options)      
    
    def toDiv(self):
        return header_template.render(header=self)

class Popover(Element):
    def __init__(self, **options):
        super(Popover, self).__init__(None, **options)
        self._icon = options.pop('icon', None)
        self._iconColour = options.pop('iconColour', None) 
        self._body = options.pop('body', '')
        self._buttonText = options.pop('buttonText', None)
        
    def _get_icon(self):
        return self._icon
    
    def _get_icon_colour(self):
        return self._iconColour
    
    def _get_body(self):
        return self._body
    
    def _get_button_text(self):
        return self._buttonText

    def toDiv(self):
        return popover_template.render(popover=self)
    
class StatPopover(Popover):
    
    def __init__(self, stats, **options):
        super(StatPopover, self).__init__(**options)
        self._icon = 'fa-info-circle fa-lg'
        self._header = 'Stats'
        self._body = StatGrid(stats, **options).toDiv()
        self.add_css_class('btn-sm btn-success')
        self.add_custom_css({'float':'right', 'max-width':'100%'})
        self.set_size(1)
        
class StatGrid(Element):
    def __init__(self, stats, **options):
        super(StatGrid, self).__init__(None, **options)
        self._stats = stats
        
    def _get_stats(self): 
        return self._stats
    
    def toDiv(self):
        return statsgrid_template.render(statsgrid=self)
    
    