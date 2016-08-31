#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一.for...in循环
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
# 依次把list或tuple中的每个元素迭代出来
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)


# range()函数
# range()函数可以生成一个整数序列,如range(5)生成的序列是从0开始小于5的整数
print(range(5))


# list()函数
print(list(range(5)))


# 计算0-100的和
sum = 0
for i in range(101):
    sum = sum + i
print(sum)


# 二.while循环
# 只要条件满足，就不断循环，条件不满足时退出循环
# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出
