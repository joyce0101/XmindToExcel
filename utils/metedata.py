#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：XmindToExcel 
@File    ：metedata.py
@Author  ：兰秋影
@Date    ：2022/6/21 2:23 PM 
"""


class TestCase(object):
    def __int__(self, title, directory, steps, expectation, priority, precondition):
        self.title = title
        self.directory = directory
        self.steps = steps
        self.expectation = expectation
        self.priority = priority
        self.precondition = precondition  # 前置条件

    def to_dict(self):
        data = {
            'title': self.title,
            'directory': self.directory,
            'steps': self.steps,
            'expectation': self.expectation,
            'priority': self.priority,
            'precondition': self.precondition  # TODO 前置条件可以写在用例标题的笔记里面，暂未实现
        }
        return data
