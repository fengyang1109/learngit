#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    :2019/6/24 17:34
import socket
import subprocess
import json
import struct



def server():
    print('server-starting'.center(30, '#'))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8888))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        # print(conn)
        # print(addr)
        while True:
            try:
                cmd = conn.recv(1024)
                if not cmd: break
                res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                       stderr=subprocess.PIPE,
                                       stdout=subprocess.PIPE)
                err = res.stderr.read()
                if err:
                    cmd_res = err
                else:
                    cmd_res = res.stdout.read()
                # 定义包含所有数据的字典
                head_dic = {'filename': None, 'totle_szie': len(cmd_res), 'hash': None}
                # 将字典序列化
                head_json = json.dumps(head_dic)
                # 将序列化后的数据转换为bytes类型
                head_bytes = head_json.encode('utf-8')
                # 首先发送报头长度
                conn.send(struct.pack('i', len(head_bytes)))
                # 在发送包头
                conn.send(head_bytes)
                # 再发送真实数据
                conn.send(cmd_res)


            except Exception:
                break
        conn.close()
    s.close()
if __name__ == '__main__':
     server()