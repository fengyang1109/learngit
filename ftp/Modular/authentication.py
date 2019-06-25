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
cg.read(r'%s\config\ftp.ini' % basedir)


def auth():
    n = 0
    while n < 3:
        user_name = input('请输入用户名>>: ').strip()
        user_pwd = input('请输入密码 >>: ').strip()
        if not user_name: continue
        # user_pwd = getpass.getpass('请输入密码 >>: ')
        if cg.has_option('user', user_name) and \
                user_pwd == cg.get('user', user_name):
            user_dic = {'user_state': True,
                        'user_name': user_name,
                        'user_pwd': user_pwd,
                        'user_home': cg.get('Home_catalogue', user_name),
                        'user_space': cg.get('data_space', user_name)}
            return user_dic
        else:
            print('用户名或密码错误')
            n += 1
    user_dic = {'user_state': False}
    return user_dic


if __name__ == '__main__':
    auth()
