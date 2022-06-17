#本次练习内容包含：迭代器next(), 生成器yield

# list=[1,4,3,63,68,5,72,777]
# #处理成迭代器
# it=iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
#生成器yield,构建迭代器
def frange(start,stop,step):
    x = start
    while x < stop:
        yield x
        x += step
for i in frange(10,20,0.5):
    print(i)



