# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 01:17:44
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 01:54:59

# This queries every database on the local 
# machine and returns the compiled result. 

from snippets import *
from get_database_names import *
import sqlite3

def run_query(sql="",db_path=""):
    if valid_select_query(sql) 
        conn = sqlite3.connect(db_path)
        with conn:
            cur = conn.cursor()
            cur.execute(sql)
            return(cur.fetchall())

# queries every database local to this machine and 
# joins the results into one array
def query_all(select_query):
    output = False
    if valid_select_query(sql):
        output = []
        for i in get_database_names():
            for ii in run_query(select_query,i):
                output.append(ii)
    return(output)

