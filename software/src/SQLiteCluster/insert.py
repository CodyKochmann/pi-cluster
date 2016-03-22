# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 02:02:36
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 15:25:00

# runs insert queries if they apply to that machine

from snippets import *
from get_database_names import *
from run_query import *

def insert(db_name,sql):
    if db_name in get_database_names(): 
        if valid_insert_query(sql):
            return(run_query(sql, db_name))
