#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# re模块
# 有了准备知识，我们就可以在Python中使用正则表达式了。Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
# r或R开头的python中的字符串表示（非转义的）原始字符串
s = r'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\\-001'

# 看看如何判断正则表达式是否匹配：
import re
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$','010 12345'))
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
