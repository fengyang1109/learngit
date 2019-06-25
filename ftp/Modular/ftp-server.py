#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 17:34
import socket
import json
import struct
class server:
    '''ftp服务端主程序'''
    def __init__(self, username, pwd, data_space, home_catalogue):
        self.username = username
        self.pwd = pwd
        self.data_space = data_space
        self.home_catalogue = home_catalogue
    def acc(self):
        ftp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_server.bind(('127.0.0.1', 2223))
        ftp_server.listen(5)
        while True:
            conn, addr = ftp_server.accept()

            while True:
                try:
                    cmd = conn.recv(1024)
                    if not cmd: break
                    res

