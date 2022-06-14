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

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_absolute_path(path):
    fp, fn = os.path.split(path)
    if not fp:
        fp = os.getcwd()
    fp = os.path.abspath(os.path.expanduser(fp))
    return os.path.join(fp, fn)


def xmind_to_excel(path):
    file_path = get_absolute_path("../xmind/中心主题.xmind")
    root = xmind_to_dict(file_path)[0]['topic']
    story_id = root["note"]


if __name__ == '__main__':
    file_path = get_absolute_path("../xmind/中心主题.xmind")
    root = xmind_to_dict(file_path)[0]['topic']
    logging.debug("parse XMind file(%s) dict data: %s", file_path, root)
    xmind_json = json.dumps(root, indent=2, ensure_ascii=False)
    with open(r'../file.json', 'w', encoding='utf8') as f:
        f.write(xmind_json)
