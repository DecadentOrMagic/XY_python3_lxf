#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 位置参数
# 定义一个计算x2的函数
# 对于power(x)函数，参数x就是一个位置参数
def power(x):
    return x * x
# 当我们调用power函数时，必须传入有且仅有的一个参数x
print(power(5))
print(power(15))

# 如果我们想计算x的n次方
# 把power(x)修改为power(x, n)，用来计算xn
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#power(x, n)函数，可以计算任意n次方
print(power(5,2))
print(power(5,3))


# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用,Python的错误信息很明确：调用函数power()缺少了一个位置参数n
# power(5)

# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 当我们调用power(5)时，相当于调用power(5, 2)
print(power(5))
print(power(5,2))

# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 例子:我们写个一年级小学生注册的函数，需要传入name和gender两个参数:
def enroll(name,gender):
    print('name',name)
    print('gender',gender)
# 这样，调用enroll()函数只需要传入两个参数：
enroll('sarah','F')
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# 我们可以把年龄和城市设为默认参数：
def enroll(name,gender,age=20,city='Qingdao'):
    print('name',name)
    print('gender',gender)
    print('age',age)
    print('city',city)
# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
enroll('Sarah', 'F')
# 只有与默认参数不符的学生才需要提供额外的信息：
# 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
# 除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
enroll('xiaoliu','男',21)
# 当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('xiaosun','男',city='青岛')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
enroll('xiaosun','男',city='青岛')


# 默认参数最大的坑
# 先定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L
# 当你正常调用时，结果似乎不错：
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
# 当你使用默认参数调用时，一开始结果也是对的：
print(add_end())
# 但是，再次调用add_end()时，结果就不对了：
print(add_end())
print(add_end())
# 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！


# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 现在无论调用多少次都不会有问题了
print(add_end())
print(add_end())


# 可变参数
# 在Python函数中，还可以定义可变参数。可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 例:给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 但是调用的时候，需要先组装出一个list或tuple：
print(calc([1,2,3]))
print(calc((1,3,5,7)))

# 把上面函数的参数改为可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 再次调用
print(calc())
print(calc(1,2,3))
print(calc(1,3,5,7))
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数,包括0个参数

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))

# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
person('Michael',30)
# 也可以传入任意个数的关键字参数
person('Bob',25,city='青岛')
person('Adam',45,gender='M',job='Engineer')
# 关键字参数的作用:它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Qingdao', 'job': 'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
# 当然，上面复杂的调用可以用简化的写法
person('Jack',24,**extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
# 仍以person()函数为例，我们希望检查是否有city和job参数
def person(name,age,**kw):
    if 'city' in kw:
        # 有city参数
        print('存在city')
    if 'job' in kw:
        # 有job参数
        print('存在job')
    print('name',name,'age',age,'other',kw)
# 但是调用者仍可以传入不受限制的关键字参数
person('Jack', 24, city='Qingdao', addr='Huangdao', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person(name,age,*,city,job):
    print(name,age,city,job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, city='Beijing', job='Engineer',school='青岛大学')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person('Jack', 24, 'Beijing', 'Engineer')
# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数

# 命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city='Qingdao',job):
    print(name,age,city,job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
person('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 比如
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去
f1(1,2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
# 最神奇的是通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

# 小结
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
