# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 17:07:14
# @Last Modified 2016-03-21
# @Last Modified time: 2016-03-21 17:26:39
def load_config(setting):
    from snippets import load_json
    config_data=load_json("SQLiteCluster/config.json")
    return(config_data[setting])
