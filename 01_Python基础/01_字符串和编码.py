#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码




# *******************
# 字符编码
# *******************
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符:
a = ord('A')
print(a)
a = ord('中')
print(a)
a = chr(66)
print(a)
a = chr(25991)
print(a)

# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')


# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# 要计算str包含多少个字符，可以用len()函数：
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))




# *******************
# 格式化
# *******************
# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
# 常见的占位符有: %d 整数    %f 浮点型    %s 字符串    %x 十六进制整数
print('Hello,%s'%'world')
print('Hi,%s,you have $%d.'%('Michael',1000000))
# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d'%(3,1))
print('%.2f'%3.1415926)
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age:%s. Gender:%s'%(25,True))
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate:%d%%'%7)
