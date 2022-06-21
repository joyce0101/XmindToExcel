#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：XmindToExcel 
@File    ：metedata.py
@Author  ：兰秋影
@Date    ：2022/6/21 2:23 PM 
"""


class TestCase(object):
    def __int__(self, title, directory, steps, expectation, priority):
        self.title = title
        self.directory = directory
        self.steps = steps
        self.expectation = expectation
        self.priority = priority
