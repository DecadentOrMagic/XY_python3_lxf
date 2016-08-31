#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过help(x)查看x函数的帮助信息
# help(abs)

# 调用abs函数(求绝对值的函数)
print(abs(100))
print(abs(-10))
print(abs(12.34))

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个
# abs(1,2)
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型
# abs('s')

# max()可以接收任意多个参数，并返回最大的那个
print(max(1,2,5,-8))

# 数据类型转换函数
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
print(bool('dafjdaldf'))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))
