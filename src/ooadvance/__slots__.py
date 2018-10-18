#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author TaoRenJie
    @file   __slots__.py
    @DATE   2018/10/18
    @Description    使用__slots__
"""


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = '231'
# s.source = '231'
print(s.name)
