#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author TaoRenJie
    @file   att.py
    @DATE   2018/10/18
    @Description    
"""
# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

class Student(object):
    name = 'Student'



print(Student.name)
s = Student()
print(s.name)
