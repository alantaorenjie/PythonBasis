#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author TaoRenJie
    @file   information.py
    @DATE   2018/10/18
    @Description    
"""

import student

# 使用type()
print(type(123))
print(type(student))
print(type('123'))
print(type(abs))


# 使用isinstance()
# 可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：


# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir(123))
print(dir('123'))
print(dir(len))