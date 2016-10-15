#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
import itertools
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
