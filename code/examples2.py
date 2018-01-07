#! /usr/bin/env python
# -*- coding: utf-8 -*-

def max_in_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max




print(max_in_list([1,3,9,15,8,7,4,6,12]))
