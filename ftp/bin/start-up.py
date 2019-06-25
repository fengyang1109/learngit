#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 17:20
import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from Modular import authentication
from Modular import ftp_client
from Modular import ftp_server
from multiprocessing import Process


def run():
    ftp_server.server()


user_dic = {}
if __name__ == '__main__':
    print('欢迎使用ftp')
    user_dic.update(authentication.auth())
    if user_dic['user_state']:
        P = Process(target=run)
        P.start()
        c1 = ftp_client.client(
            user_dic['user_name'],
            user_dic['user_pwd'],
            user_dic['user_home'],
            user_dic['user_space']
        )
        c1.starting()
