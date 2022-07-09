#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：XmindToExcel 
@File    ：xmind_parser.py
@Author  ：兰秋影
@Date    ：2022/6/13 3:14 PM 
"""

import os
import logging
import json
from xmindparser import xmind_to_dict


config = {
    'title': '#'
}
case_list = []


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_absolute_path(path) -> str:
    """
    :param path: xmind 文件路径
    :return: 文件绝对路径
    """
    fp, fn = os.path.split(path)
    if not fp:
        fp = os.getcwd()
    fp = os.path.abspath(os.path.expanduser(fp))
    return os.path.join(fp, fn)


def xmind_to_excel(path) -> list:
    """
    :param path:
    :return: 解析后的用例列表
    """
    file_path = get_absolute_path("../xmind/中心主题.xmind")
    root = xmind_to_dict(file_path)[0]['topic']
    logging.debug("parse XMind file(%s) dict data: %s", file_path, root)
    story_id = root["note"]


def write_excel(case_list):
    pass


def is_testcase_topic(case_dict):
    """
    topic有标题标记
    :param case_dict: dict topic
    :return:
    """
    flag = config['title']
    if flag in case_dict['title']:
        return True


def parse_case(case_dict, parent_node):
    """
    解析用例
    :param case_dict:
    :param parent_node:
    :return:
    """
    pass


if __name__ == '__main__':
    # file_path = get_absolute_path("../xmind/中心主题.xmind")
    # root = xmind_to_dict(file_path)[0]['topic']
    # logging.debug("parse XMind file(%s) dict data: %s", file_path, root)
    # xmind_json = json.dumps(root, indent=2, ensure_ascii=False)
    # with open(r'../file.json', 'w', encoding='utf8') as f:
    #     f.write(xmind_json)
    pass
