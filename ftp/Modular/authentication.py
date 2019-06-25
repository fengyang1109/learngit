#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 17:35
import configparser
import getpass
import os
import sys
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

cg = configparser.ConfigParser()
cg.read(r'I:%s\config\ftp.ini' %basedir)

print(cg.sections())
# while True:
#     user_name = input('请输入用户名>>: ')
#     user_pwd = input('请输入密码>>: ')