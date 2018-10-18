#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author TaoRenJie
    @file   Screen.py
    @DATE   2018/10/18
    @Description  请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
"""


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


s = Screen()
s.width = 10
s.height = 20
print(s.resolution)
