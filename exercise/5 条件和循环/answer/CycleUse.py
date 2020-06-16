# 练习二 循环语句的使用
# 1. 使用for语句输出1-100之间的所有偶数
# for number in range(1,100):
#     if number%2==0:
#         print(number)
# 2. 使用while语句输出1-100之间能够被3整除的数字
import time
num=1
while True:
    if num%3==0:
        print(num)
        # time.sleep(1)
    elif num>100:
        break
    num = num + 1