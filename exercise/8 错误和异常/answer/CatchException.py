# 练习一 异常
# 1. 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# i=j
# Traceback (most recent call last):
#   File "C:/Users/gaoli/geekbangpython/exercise/8 错误和异常/answer/CatchException.py", line 3, in <module>
#     i=j
# NameError: name 'j' is not defined
# alist=['xyz','zbc']
# alist[4]
# Traceback (most recent call last):
#   File "C:/Users/gaoli/geekbangpython/exercise/8 错误和异常/answer/CatchException.py", line 9, in <module>
#     alist[4]
# IndexError: list index out of range
# dict1={'x':1,'y':2}
# dict1['z']
# Traceback (most recent call last):
#   File "C:/Users/gaoli/geekbangpython/exercise/8 错误和异常/answer/CatchException.py", line 15, in <module>
#     dict1['z']
# KeyError: 'z'
# 2. 通过Python程序产生IndexError，并用try捕获异常处理
try:
    alist=['xyz','zbc']
    alist[4]
except Exception as e:
    print(e)
