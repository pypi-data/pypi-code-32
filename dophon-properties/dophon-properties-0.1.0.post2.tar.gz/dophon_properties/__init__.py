import sys
import re
from dophon_properties import tools

__version__ = '0.1.0'

LOGGER_ROOT = 'dophon_properties.'

PROP_FUN = '.properties'

MQ = {
    'name': 'mq',
    'modules': [
        'dophon_mq.properties',
        'dophon_mq.properties.properties',
        'dophon.mq.properties',
        'dophon.mq.properties.properties'
    ]
}

DOPHON = {
    'name': 'main',
    'modules': [
        'properties',
        'dophon.properties'
    ]
}


@tools.module_edge_print('properties module')
def get_properties(prop_type: dict):
    m = __import__(LOGGER_ROOT + prop_type['name'] + PROP_FUN, fromlist=True)
    init_result = eval('m.init_properties()')
    for module_alias in prop_type['modules']:
        sys.modules[module_alias] = init_result
    # 打印模块信息
    for name in dir(init_result):
        if not re.match('^__.+__$', name):
            print(name, '---', getattr(init_result, name))

