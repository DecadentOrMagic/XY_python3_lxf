#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。
# 要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
# pip3 install Pillow
# 有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
from PIL import Image
im = Image.open('CELTICS_200*200.png')
print(im.format,im.size,im.mode)

im.thumbnail((200, 100))
im.save('thumb.png','PNG')
# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
# import mymodule
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
import sys
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
import sys
sys.path.append('/Users/xueyao/Desktop/后端开发/Python/XY_python3_lxf')
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
