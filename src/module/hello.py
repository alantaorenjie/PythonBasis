#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author TaoRenJie
    @file   hello.py
    @DATE   2018/10/18
    @Description    
"""

import sys
import platform

def test():


    print(platform.python_version())
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
