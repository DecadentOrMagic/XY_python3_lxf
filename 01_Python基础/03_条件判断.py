#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')
# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
# 注意不要少写了冒号:
age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')
# 可以用elif做更细致的判断
age = 7
if age >= 18:
    print('your age is',age)
    print('adult')
elif age >= 6:
    print('your age is',age)
    print('teenager')
else:
    print('your age is',age)
    print('kid')
# if判断条件还可以简写,只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = ['1''2']
if x:
    print('Ture')

# int()函数
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
# int()函数发现一个字符串并不是合法的数字时就会报错
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
