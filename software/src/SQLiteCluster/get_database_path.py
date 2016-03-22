# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 14:09:08
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 14:36:47

from snippets import *

# finds the reverse index in an object
def reverse_index(needle,haystack):
    index = -1
    output= -1
    for i in haystack:
        index+=1
        if i == needle:
            output = index
    return output

# returns the directory containing the sqlite dbs
def get_database_path():
    db_path = current_dir().split("/")
    db_path = db_path[:reverse_index("src", db_path)+1]
    return("/".join(db_path)+"/db/")
