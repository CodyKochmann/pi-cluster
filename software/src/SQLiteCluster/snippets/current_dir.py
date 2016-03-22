# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 14:02:43
# @Last Modified 2016-03-22me>
# @Last Modified time: 2016-03-22 14:02:56

def current_dir(): 
    # returns a unix current directory
    # By: Cody Kochmann
    from os import path
    return(path.dirname(path.realpath(__file__)))
