#coding=utf-8
from distutils.core import setup
setup(
    name="rongMathoo", #对外发布的模块名字
    version="1.0",  #版本号
    description='这是第一个对外发布的模块，里面只有数学方法，用于测试哦',  #描述
    author="ronger",  #作者
    author_email="398128284@qq.com",  #作者邮箱
    py_modules=["rongMathoo.demo1","rongMathoo.demo2"]   #要发布的模块
)