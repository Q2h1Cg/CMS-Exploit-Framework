#!/usr/bin/env python
# -*- coding:utf-8 -*-

from termcolor import colored


def error(string):
    """
    输出错误信息
    :param string: string, 欲输出的信息
    :return:
    """
    print colored("[!]"+string, "red")


def success(string):
    """
    输出成功信息
    :param string: string, 欲输出的信息
    :return:
    """
    print colored("[+]"+string, "green")


def process(string):
    """
    输出进程中信息
    :param string: string, 欲输出的信息
    :return:
    """
    print colored("[*]"+string, "blue")