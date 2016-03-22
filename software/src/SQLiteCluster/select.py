# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 01:17:44
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 15:26:50

# This queries every database on the local 
# machine and returns the compiled result. 

from snippets import *
from get_database_names import *
import sqlite3

def run_select_query(sql,db_name):
    if valid_select_query(sql):
        result = run_query(sql, db_name)

# queries every database local to this machine and 
# joins the results into one array
def select(select_query):
    output = False
    if valid_select_query(sql):
        output = []
        for i in get_database_names():
            try:
                for ii in run_select_query(select_query,i):
                    output.append(ii)
            except:
                pass
    return(output)

