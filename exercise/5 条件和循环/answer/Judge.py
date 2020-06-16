# 练习一 条件语句的使用

#1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
string=input("请输入字符串：")
if len(string)==10:
    print("'%s'字符串长度为10" %(string))
else:
    print("'%s'字符串长度小于10" %(string))
#2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
number=int(input("请输入一个1-40的数字："))
if number>=1 and number<=10:
    print('"%s"数字在1到10之间' %(number))
elif 10<number<=20:
    print('"%s"数字在10到20之间' %(number))
elif 20<number<=30:
    print('"%s"数字在20到30之间' % (number))
elif 30<number<=40:
    print('"%s"数字在30到40之间' % (number))