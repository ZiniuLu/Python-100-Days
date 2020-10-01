"""

第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 骆昊
Date: 2018-02-26

请将该文件命名为hello.py并在终端中通过下面的命令运行它
python hello.py

"""

print('hello, world!')
# print("你好,世界！")
print('你好', '世界')
print('hello', 'world', sep=', ', end='!')
print('goodbye, world', end='!\n')


#mWrite a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program

l=[]
t=()
for i in range(5):
	my_num=int(input(print("hey type ur number i, will convert it into list and tuple")))
	l.append(my_num)
print(tuple(l))



print(l)
print()


