import os
import json
import sys
from ruamel import yaml
from jinja2 import Environment

from cpbox.tool import file
from cpbox.tool import array

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def load_json(file, fallback=None):
    if not os.path.isfile(file):
        return fallback
    data = None
    with open(file, 'r') as f:
        data = json.load(f)
    return data if data is not None else fallback

def load_yaml(file, fallback=None):
    if not os.path.isfile(file):
        return fallback
    data = None
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    return data if data is not None else fallback

def load_yaml_from_dir(dir):
    if not os.path.isdir(dir):
        return fallback
    file_list = file.listdir(dir)
    data = {}
    for path in file_list:
        if '.yml' not in path and '.yaml' not in path:
            continue
        data = array.merge(data, load_yaml(path, {}))
    return data

def load_yaml_config(config_file, config_section=None, extra_kvs=None):
    config = load_yaml(config_file, {})
    if config_section is not None:
        key_list = config_section.split('.')
        for sub_key in key_list:
            if sub_key not in config:
                raise Exception('Can not find config section for sub key:' +  sub_key)
            config = config[sub_key]

    if extra_kvs is not None:
        config.update(extra_kvs)
    return config

def dump_json(data, file, **kwargs):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, **kwargs)

def pjson(data):
    return json.dumps(data, indent=2, sort_keys=True)

def pyaml(data):
    yaml.Dumper.ignore_aliases = lambda *args : True
    return yaml.dump(data, default_flow_style=False)

def dump_yaml(data, file):
    with open(file, 'w') as outfile:
        yaml.safe_dump(data, outfile, default_flow_style=False)

def json_to_yaml(src, out):
    data = load_json(src)
    dump_yaml(data, out)
