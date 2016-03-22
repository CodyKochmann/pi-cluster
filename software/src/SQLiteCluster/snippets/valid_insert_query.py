# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 02:12:34
# @Last Modified 2016-03-22me>
# @Last Modified time: 2016-03-22 02:13:03

from contains_only_whitelisted import *

# returns bool if valid insert query    
def valid_insert_query(sql):
    # if the sql is empty
    if len(sql.split(' '))>1:
        return(False)
    # no semicolons
    if ";" in sql:
        return(False)
    # only whitelisted characters are allowed
    whitelist="abcdefghijklmnopqrstuvwxyz0123456789- "
    if contains_only_whitelisted(sql.lower(), whitelist) is False:
        return(False)
    # the first word has to be insert
    if (sql.split(' ')[0]).lower() is not "insert":
        return(False)
    return(True)