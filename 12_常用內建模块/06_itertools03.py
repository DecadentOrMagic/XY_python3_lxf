#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
import itertools
for key, group in itertools.groupby('ABAABBBCCAAA'):
    print(key, list(group))


# 小结
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
