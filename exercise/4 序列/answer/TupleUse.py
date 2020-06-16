# 练习四 元组的基本操作

# 1. 定义一个任意元组，对元组使用append() 查看错误信息
tupleString=("aaa",'bbb',1)
print(tupleString)
#tupleString.append('asdsa')
# 2. 访问元组中的倒数第二个元素
print(tupleString[len(tupleString)-2])
print(tupleString[-2])
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
tupleString1 = ("ccc","dddd")
print(tupleString+tupleString1)
# 4. 计算元组元素个数
print(len(tupleString+tupleString1))
print((tupleString+tupleString1).__len__())