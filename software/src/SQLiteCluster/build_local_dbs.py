# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 00:40:51
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 14:32:33

# builds the local databases for this server

from snippets import *
from get_database_names import *
from get_database_path import *

def build_local_dbs():
    db_path = get_database_path()
    for i in get_database_names():
        i = db_path + i 
        if file_exists(i) is False:
            create_sqlite_db(i)
        else:
            log("%s - already exists")
    return
