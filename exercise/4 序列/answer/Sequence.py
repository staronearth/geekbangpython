# 练习三 列表的基本操作

# 1. 定义一个含有5个数字的列表
sequence=[5,10,15,25,30]
# 2. 为列表增加一个元素 100
sequence.append(100)
sequence.append("abc")
print(sequence)
# 3. 使用remove()删除一个元素后观察列表的变化
sequence.remove(10)
print(sequence)
# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
print(sequence[0:3])