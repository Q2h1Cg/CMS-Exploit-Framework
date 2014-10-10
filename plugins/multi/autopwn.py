#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib import logger
from lib import plugin_manager
from lib import threadpool

author = "Chu <root@sh3ll.me>"
scope = "All CMS"
description = "漏洞批量利用模块"
reference = "http://sh3ll.me/"
options = [
    {
        "Name": "Plugins",
        "Current Setting": "All",
        "Required": True,
        "Description": "插件列表"
    },
    {
        "Name": "Target",
        "Current Setting": "",
        "Required": False,
        "Description": "网站地址"
    },
    {
        "Name": "Target_file",
        "Current Setting": "",
        "Required": False,
        "Description": "网站地址文件"
    },
    {
        "Name": "WhatWeb",
        "Current Setting": "Y",
        "Required": True,
        "Description": "网站地址"
    },
    {
        "Name": "Thread",
        "Current Setting": "5",
        "Required": True,
        "Description": "线程数"
    },
]


class NoTarget(Exception):
    """
    未设置 Target 时的异常
    """

    def __init__(self):
        self.message = "Target or Target_file must be setted"


class AutoPwn(plugin_manager.PluginManager):
    """
    Auto Pwn
    """

    def __init__(self, plugins, what_web, thread_number, target=None,
                 target_file=None):
        plugin_manager.PluginManager.__init__(self)
        if plugins == "All":
            self.enable_plugins = (p[0] for p in self.list_plugins()
                                   if not p[0].startswith("multi_"))
        else:
            self.enable_plugins = plugins.split(",")
        self.options = options
        if not (target or target_file):
            raise NoTarget
        elif target:
            self.targets = {target: ""}
        else:
            with open(target_file) as f:
                self.targets = {i.strip(): "" for i in f}
        self.what_web = True if what_web == "Y" else False
        self.thread_number = thread_number
        self.vulns = []

    def load_plugins(self):
        """
        加载所有插件
        :return:
        """
        for plugin_name in self.enable_plugins:
            self.load_plugin(plugin_name)
            if not (len(self.plugins[plugin_name]["options"]) == 1
                    or (len(self.plugins[plugin_name]["options"]) == 2
                        and "Thread" in self.plugins[plugin_name]["options"])):
                self.plugins.pop(plugin_name)

    def identify_cms(self):
        """
        批量指纹识别
        :return:
        """
        self.load_plugin("multi_whatweb")
        for target in self.targets:
            self.set_option("URL", target)
            result = self.exec_plugin()
            if result[0]:
                self.targets[target] = result[1].split(": ")[1]
        self.plugins.pop("multi_whatweb")

    def exec_single_plugin(self, target):
        """
        执行单个插件
        :param target: str, 目标站点地址
        :return:
        """
        target_cms = self.targets[target]
        if not target_cms or self.current_plugin.startswith(target_cms):
            self.set_option("URL", target)
            vuln = self.exec_plugin()
            if vuln[0]:
                self.vulns.append((self.current_plugin, vuln[1]))

    def log_vulns(self):
        """
        保存并输出结果
        :return:
        """
        for plugin, vuln in self.vulns:
            self.cu.execute("insert into vulns values (?, ?)", (plugin, vuln))
            self.conn.commit()
        print "\nVulns\n=====\n"
        print "%-40s%s" % ("Plugin", "Vuln")
        print "%-40s%s" % ("------", "----")
        for plugin, vuln in self.vulns:
            print "%-40s%s" % (plugin, vuln)
        print

    def exec_plugins(self):
        """
        执行所有插件
        :return:
        """
        logger.process("Loading Plugins")
        self.load_plugins()
        if self.what_web:
            logger.process("Loading multi_whatweb")
            self.identify_cms()
        for plugin in self.plugins:
            logger.process("Loading %s" % plugin)
            self.load_plugin(plugin)
            pool = threadpool.ThreadPool(self.thread_number)
            reqs = threadpool.makeRequests(self.exec_single_plugin,
                                           self.targets)
            for req in reqs:
                pool.putRequest(req)
            pool.wait()
        self.log_vulns()


def exploit(Plugins, Target, Target_file, WhatWeb, Thread):
    autopwn = AutoPwn(Plugins, WhatWeb, Thread, Target, Target_file)
    autopwn.exec_plugins()
    autopwn.exit()
    return "Finished"