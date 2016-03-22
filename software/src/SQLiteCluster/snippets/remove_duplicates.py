# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 01:49:26
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 01:51:46

def remove_duplicates(input_list=[]):
    output = []
    while(len(input_list)>0):
        tmp = input_list.pop()
        if tmp not in output:
            output.append(tmp)
    return(output)
