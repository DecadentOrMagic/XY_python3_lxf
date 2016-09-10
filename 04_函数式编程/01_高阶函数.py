#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 变量可以指向函数
# 以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
print(abs(-10))
# 如果只写abs呢
# print(abs)
# 可见，abs(-10)是函数调用，而abs是函数本身。
# 要获得函数调用结果，我们可以把结果赋值给变量：
x = abs(-10)
print(x)
# 如果把函数本身赋值给变量
f = abs
# print(f)
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# 如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？
print(f(-10))
# 说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。


# 函数名也是变量
# 函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
# 如果把abs指向其他对象
# abs = 10
# print(abs(-10))
# print(abs)
# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！
# 当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。
# 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。


# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 一个最简单的高阶函数：
def add(x,y,f):
    return f(x) + f(y)
print(add(-5,6,abs))
# 编写高阶函数，就是让函数的参数能够接收别的函数。
