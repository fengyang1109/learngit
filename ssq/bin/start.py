#!/usr/bin/env python
# -*- coding:utf8 -*-
# auth:fy

import os
import sys

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from model import contrast
from model import write
# from model import ipt
write.wri()
contrast.con()

