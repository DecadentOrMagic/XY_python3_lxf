#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
print('a b   c'.split(' '))
print('a b   c'.split('  '))
# 无法识别连续的空格，用正则表达式试试：
import re
print(re.split(r'\s+', 'a b  c'))
# 无论多少个空格都可以正常分割。加入,试试：
print(re.split(r'[\s\,]+', 'a,b, c  d'))
# 再加入;试试：
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
# 如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。
