#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
# dict的key必须是不可变对象,字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d)
print(d['Bob'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 80
print(d)
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Michael'] = 100
print(d)
# 如果key不存在，dict就会报错
# print(d['Thomas'])

# 避免key不存在的错误
# 一.通过in判断key是否存在
print('Thomas' in d)
# 二.通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas',-1))

# 用pop(key)方法删除一个key,对应的value也会从dict中删除
d.pop('Bob')
print(d)


# Set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的

# 重复元素在set中自动被过滤
s = set([1,1,2,3,4,3,2,5,4])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(6)
print(s)
s.add(6)
print(s)

# 通过remove(key)方法可以删除元素
s.remove(6)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1|s2)

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素
