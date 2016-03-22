# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 02:19:57
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 15:24:43
from get_database_path import *

def run_query(sql,db_name):
    import sqlite3
    conn = sqlite3.connect(get_database_path() + db_name)
    output = False
    try:
        with conn:
            cur = conn.cursor()
            cur.execute(sql)
            output=cur.fetchall()
            conn.commit()
    except Exception, e:
        log(e)
        conn.rollback()
    conn.close()
    return(output)
