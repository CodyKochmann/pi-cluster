# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 00:40:51
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 01:07:02

# builds the local databases for this server

from snippets import *
from get_database_names import *

def build_local_dbs():
    for i in get_database_names():
        if file_exists(i) is False:
            log("creating %s"%(i))
            create_sqlite_db(i)
    return
