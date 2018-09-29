#!/usr/bin/env python
# -*- coding:utf8 -*-
# __auth__:fy

"""
融合模块
"""

import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from model import oddandeven
from model import select


def fs():
	oe = oddandeven.oad()
	se = select.ball_select()

if __name__ == '__main__':
	fs()
