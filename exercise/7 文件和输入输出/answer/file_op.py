
# 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期
import time
datefile = open('date.txt','w')
print(time.time())
print(time.asctime(time.localtime(time.time())))
formattime=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
datefile.write(formattime)
datefile.close()
# 2. 再次打开这个文件，读取文件的前4个字符后退出
datefile1 = open('date.txt')
string = datefile1.read(4)
print(string)
datefile1.close()