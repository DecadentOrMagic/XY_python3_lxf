#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。
# datetime
# datetime是Python处理日期和时间的标准库。


# 1.获取当前日期和时间
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。




# 2.获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2016, 10, 11, 19, 50) # 用指定日期时间创建datetime
print(dt)
