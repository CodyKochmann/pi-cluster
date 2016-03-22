# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 01:29:32
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 01:40:48

from contains_only_whitelisted import *

# returns bool if valid select query    
def valid_select_query(sql):
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
    # the first word has to be select
    if (sql.split(' ')[0]).lower() is not "select":
        return(False)
    return(True)