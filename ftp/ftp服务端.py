#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 16:23
import socket
import configparser
import os
import sys
import json
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
ftp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ftp_server.bind(('127.0.0.1', 2223))
ftp_server.listen(5)
config = configparser.ConfigParser()
config.read(r'I:\\py项目\ssq\ftp.ini')
while True:

    conn, addr = ftp_server.accept()
    print('start>>>>>>>>>>>>>')
    res = conn.recv(4)
    user_bytes = conn.recv(len(res))
    print(user_bytes)


