# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 14:37:55
# @Last Modified by:   CodyKochmann
# @Last Modified time: 2016-03-21 14:48:39

# returns the contents of a file
def read_file(file_path):
    with open(file_path,'r') as f:
        return(f.read())

# creates or updates a file with the given text
def write_file(file_path,text_to_write):
    with open(file_path,'w') as f:
        f.write(text_to_write)
        return

# returns a boolean if the file exists
def file_exists(file_path):
    from os import path
    if(path.isfile(fname)):
        if(len(read_file(file_path))>0):
            return(True)
    return(False)

# loads a json file
def load_json_file(file_path):
    from json import loads
    return(loads(read_file(file_path)))
