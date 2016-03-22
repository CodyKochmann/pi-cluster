# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 01:32:01
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 01:33:40
# returns true if string is only made of the given whitelist

def contains_only_whitelisted(target,whitelist):
    for i in target:
        if i not in whitelist:
            return(False)
    return(True)