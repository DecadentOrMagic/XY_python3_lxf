#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 引入Python自带的unittest模块
import unittest

from mydict import Dict

class TestDict(unittest.TestCase): # 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
    def test_init(self): # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1) # 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d.key, 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): # 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): # 通过d.empty访问不存在的key时，我们期待抛出AttributeError
            value = d.empty


# 运行单元测试
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()

# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
# python3 -m unittest mydict_test
