# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 02:02:36
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 02:23:02

# runs insert queries if they apply to that machine

from snippets import *
from get_database_names import *

def insert(db_path,insert_sql):
    if "db/" not in db_path:
        db_path="db/%s"%(db_path)
    if db_path in get_database_names(): 
        if valid_insert_query(sql):
            return(run_query(sql, db_path))
