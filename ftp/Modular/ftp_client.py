#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 17:34
import socket
import struct
import json


class client:
    def __init__(self, username, pwd, home_catalogue, data_space):
        self.username = username
        self.pwd = pwd
        self.data_space = data_space
        self.home_catalogue = home_catalogue

    def starting(self):
        self.username = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username.connect(('127.0.0.1', 8888))
        print('client-starting>>>>>>>>>>')
        while True:

            cmd = input('>>: ').strip()
            if not cmd: continue
            self.username.send(cmd.encode('utf-8'))
            # 首先接收固定长度的报头长度数据
            head_struct = self.username.recv(4)
            # 解析报头长度
            head_len = struct.unpack('i', head_struct)[0]
            # 再接收bytes类型的报头数据
            head_bytes = self.username.recv(head_len)
            # 反序列化报头字典
            head_json = head_bytes.decode('utf-8')
            head_dic = json.loads(head_json)

            total_size = head_dic['totle_szie']
            recv_szie = 0
            data = b''
            while recv_szie < total_size:
                # 先接收1024长度
                recv_data = self.username.recv(1024)
                # 序列化数据
                data += recv_data
                # 长度递增
                recv_szie += len(recv_data)
            print(data.decode('gbk'))

        self.username.close()


if __name__ == '__main__':
    p1 = client('zhangsan', '123', 'I:\home\zhangsan', '50M')
    p1.starting()
