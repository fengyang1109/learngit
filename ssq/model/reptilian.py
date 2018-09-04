#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy
"""
抓取网页
"""
import requests
import re

"""
在线抓取方式
"""


def rep():
	print('网页抓取中................')
	url = r'http://datachart.500.com/ssq/history/history.shtml'
	page_dic = {}
	page = requests.get(url)
	# print(page.text)  #.text按页面编码 返回字符串
	if page.ok:
		tbody_str = re.findall(r'<tbody id="tdata">(.*?)</tbody>', page.text, re.S | re.M)  # 匹配tbody字段
		# print(tbody_str)
		tr_str = re.findall(r'<tr class="t_tr1">(.*?)</tr>', tbody_str[0], re.S | re.M)  # 匹配tr字段
		# print(tr_str)
		for i in range(len(tr_str)):
			res_list = []
			td_str = re.findall(r'<td>(.*?)</td>', tr_str[i], re.S | re.M)  # 匹配td字段
			# print(td_str)
			td_str_cfont = re.findall(r'<td class="t_cfont\d">(\d{2})</td>', tr_str[i], re.S | re.M)  # 匹配td class=cfont 字段
			# print(td_str_cfont, td_str[1])
			stage = '20%s' % td_str[1]  # 期号拼接
			ball_num = '{},{},{},{},{},{},{}'.format(*td_str_cfont)
			# print(i, stage, ball_num)
			res_list.append(stage)
			res_list.append(ball_num)
			page_dic[i] = res_list
		print('抓取完成')
		return page_dic
	else:
		print(page.status_code, '抓取失败')



"""
复制网页抓取方式
"""
# def rep():
# 	page_dic = {}
# 	with open(r'C:\Users\FY\Desktop\1.htm', 'r') as f:
# 		file = f.read()
#	tbody_str = re.findall(r'<tbody id="tdata">(.*?)</tbody>', file, re.S | re.M)
# 	tr_str = re.findall(r'<tr class="t_tr1">(.*?)</tr>', tbody_str[0], re.S | re.M)
# 	# print(len(tr_str))
# 	for i in range(len(tr_str)):
# 		res_list = []
# 		td_str = re.findall(r'<td>(.*?)</td>', tr_str[i], re.S | re.M)
# 		# print(td_str)
# 		td_str_cfont = re.findall(r'<td class="t_cfont\d">(\d{2})</td>', tr_str[i], re.S | re.M)
# 		# print(td_str_cfont, td_str[1])
# 		stage = '20%s' % td_str[1]
# 		ball_num = '{},{},{},{},{},{},{}'.format(*td_str_cfont)
# 		# print(i, stage, ball_num)
# 		res_list.append(stage)
# 		res_list.append(ball_num)
# 		page_dic[i] = res_list
# 	# print(page_dic)
# 	return page_dic


if __name__ == '__main__':
	rep()
