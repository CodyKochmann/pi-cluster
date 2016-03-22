# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 01:04:38
# @Last Modified 2016-03-22me>
# @Last Modified time: 2016-03-22 01:06:07
# easy control to point the logs in a certain direction for debugging

#global verbose_logging 
verbose_logging = True

def log(s):
    global verbose_logging
    if verbose_logging:
        print(s)