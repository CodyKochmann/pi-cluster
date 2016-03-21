# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 17:35:57
# @Last Modified 2016-03-21
# @Last Modified time: 2016-03-21 17:57:52

from snippets import *
from load_config import *

def find_correct_db(index,pi_count,dbs_per_pi):
    pi_number=(index/4)+1
    db_number=(index%4)+1 
    output="pi-%s.%s.db"%(pi_number,db_number)
    return(output)

def get_next_database():
    # gets the last database, 
    # adds one, and returns which
    # server and which database is next.
    last_db = load_config("last_db")
    pi_count=load_config("pi_count")
    dbs_per_pi=load_config("dbs_per_pi")
    output = last_db+1
    print("the last db was: %s"%(last_db))
    if output > ((pi_count*dbs_per_pi)-1):
        set_config("last_db",0)
        output=0
    else:
        set_config("last_db",output)
    output = find_correct_db(output,pi_count,dbs_per_pi)
    return(output)
