#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 5.str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
from datetime import datetime
cday = datetime.strptime('2016-10-11 20:25:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))
# 注意转换后的datetime是没有时区信息的。




# 6.datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(type(now.strftime('%a, %b %d %H:%M')))
