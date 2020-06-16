# 练习一 字符串

# 1. 定义一个字符串Hello Python 并使用print( )输出
hello_python='Hello Python'
print(hello_python)

# 2. 定义第二个字符串Let‘s go并使用print( )输出
let_go="Let's go"
print(let_go)
# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出
string = '"The Zen of Python" -- by Tim Peters'
print(string)

# 练习二 字符串基本操作

# 1. 定义两个字符串分别为 xyz 、abc
character_string1='xyz'
character_string2='abc'
# 2. 对两个字符串进行连接
character_string3=character_string1+character_string2
print(character_string3)
# 3. 取出xyz字符串的第二个和第三个元素
character_string4=character_string1[1:3]
print(character_string4)
# 4. 对abc输出10次
character_string5=character_string2*10
print(character_string5)
# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
character=input("请输入一个字符：")
if character in character_string1:
    print(character_string1)
elif character in character_string2:
    print(character_string2)
else:
    print('%s不在 %s和 %s字符串中' %(character,character_string1,character_string2))