#本次练习包含内容：lambda表达式；常用的内置函数：filter, map, redyce, zip

#lambda表达式 lambda 函数的变量：return返回的表达式
# def add(x,y):
#     return x+y
# print(add(2,1))
# #用lambda表示：
# lambda x,y: x+y

#————————————————————————————————————————
#内置函数
#1.filter(function or none,iterable) 筛选
a=[1,2,3,4,5,6,7]
print('filter函数：',list(filter(lambda x: x>2,a)))

#2.map(function,*iterable) 对列表中的参数依次处理    *iterable可变长参数
a=[1,2,3,4,5,6,7]
print(list(map(lambda x: x,a)))
print(list(map(lambda x: x+1,a)))
b=[6,5,3]
print('map函数：',list(map(lambda x,y: x+y,a,b)))


#3.reduce(function,sequence[,初始值（可为空）]
#使用reduce前，需先执行导入操作
from functools import reduce
print('reduce函数：',reduce(lambda x,y:x+y,[1,4,6],2))

#4.zip(object) 整合函数；对调字典中key和value的值
a=(1,3,5)
b=(2,4,6)
for i in zip(a,b):
    print('zip函数：',i)

#————————————对调字典中key和value的值
dict1 = {'a':'aa','b':'ss'}
dict2 = zip(dict1.values(),dict1.keys())
print(dict(dict2))