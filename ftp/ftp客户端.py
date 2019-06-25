#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 16:23
import socket
import json
import struct
ftp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ftp_client.connect(('127.0.0.1', 2223))
print('请输入用户名密码')
input_user = input('>>: ')
input_pwd = input('>>: ')
user_dic = {input_user: input_pwd}
user_josn = json.dumps(user_dic)
user_bytes = user_josn.encode('utf-8')
ftp_client.send(struct.pack('i', len(user_bytes)))
ftp_client.send(user_bytes)