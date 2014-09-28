#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "Demo"
description = "Plugin Demo"
reference = "http://sh3ll.me/"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    },
    {
        "Name": "Thread",
        "Current Setting": "10",
        "Required": False,
        "Description": "线程数"
    },
]


def exploit(URL, Thread):
    logger.process("Request "+URL)
    r = requests.get(URL)
    r.close()
    if r.status_code == 200:
        logger.success("200")
        return "200"
