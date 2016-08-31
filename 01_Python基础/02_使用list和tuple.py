#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# List

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 变量classmates就是一个list
# *************************************
classmates = ['Michael','Bob','Tracy']
print(classmates)
# 获取list元素的个数
print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
# 以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-2])
print(classmates[-3])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
# *************************************
classmates.append('Adam')
print(classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
# *************************************
classmates.pop()
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
# *************************************
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
# *************************************
L = ['Apple',123,True]
print(L)

# list元素也可以是另一个list
# *************************************
s = ['python','java',['asp','php'],'scheme']
print(s)
print(len(s))
# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了
p = ['asp','php']
s = ['python','java',p,'scheme']
print(s)
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到




# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# *************************************
classmates = ('Michael','Bob','Tracy')
# classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如
t = (1,2)
print(t)
# 如果要定义一个空的tuple，可以写成()
t = ()
print(t)

# *************************************
# t = (1)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

# “可变的”tuple
# *************************************
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
