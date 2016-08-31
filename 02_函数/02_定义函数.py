
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 自定义求绝对值的my_abs函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
# 调用my_abs函数
print(my_abs(-100))


# 空函数  如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来,缺少了pass，代码运行就会有语法错误
age = 20
if age > 18:
    pass


# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# my_abs(1, 2)
# 如果参数类型不对，Python解释器就无法帮我们检查
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
# my_abs('s')

# 完善my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
        if x > 0:
            return x
        else:
            return -x
# my_abs('A')


# 返回多个值
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值
r = move(100,100,60,math.pi/6)
print(r)
# 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
