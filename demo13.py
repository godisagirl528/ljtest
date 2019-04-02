# python包 有__init__.py

# 包：可以被其他py模块引用

# py文件就一个模块

from utils.demo12 import read_excel

from utils.demo9 import PySelenium

#同级
from demo9 import PySelenium

driver = PySelenium()