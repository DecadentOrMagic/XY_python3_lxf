#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 7.datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))
# 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。
