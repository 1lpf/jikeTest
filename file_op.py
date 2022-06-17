##文件的输入和输出

# #打开文件,W表示可编辑
# a=open('python练习.txt','w')
# a.write('极客时间教程')
# a.close()
#
# #增加文件内容，关键字用a
# x=open('python练习.txt','a')
# x.write('自动脚本练习')
# x.close()
#
# #读取文件
# b=open('python练习.txt')
# print(b.read())
# b.close()

# #按行读取
# #显示首行
# y=open('python练习.txt')
# print(y.readline())
# #逐行显示
# z=open('python练习.txt')
# for line in z.readlines():
#     print(line)
#     print('---')

#移动seek
m=open('python练习.txt')
print(m.tell())
print(m.read(5))
m.seek(3)
print(m.tell())
print(m.read())