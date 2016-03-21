# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 17:07:14
# @Last Modified 2016-03-21
# @Last Modified time: 2016-03-21 17:49:50
from snippets import *

def load_config(setting):
    config_path="SQLiteCluster/config.json"
    config_data=load_json(config_path)
    return(config_data[setting])

def set_config(setting,preference):
    from json import dumps
    config_path="SQLiteCluster/config.json"
    config_data = load_json(config_path)
    config_data[setting]=preference
    write_file(config_path, dumps(config_data))

