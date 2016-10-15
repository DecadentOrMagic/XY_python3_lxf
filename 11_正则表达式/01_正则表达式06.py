#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2.用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
import re
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
