#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# collections是Python内建的一个集合模块，提供了许多有用的集合类。


# 1.namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
p = (1, 2)
print(p)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 可以验证创建的Point对象是tuple的一种子类：
print(isinstance(p, Point))
print(isinstance(p, tuple))
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle',['x', 'y', 'r'])
c = Circle(0, 0, 10)
print(c)
