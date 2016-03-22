# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 02:19:57
# @Last Modified 2016-03-22me>
# @Last Modified time: 2016-03-22 02:20:34
 
def run_query(sql,db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
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
