# # 记录12生肖，根据年份判断生肖
# shengxiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
#
#
# #xingzuo_name =('水瓶座','白羊座','双鱼座')
# #xingzuo_days =((1,20),(2,19),(3,21))
#
# year = int(input('请输入出生年份'))
# if(shengxiao[year%12])=='虎':
#     print("是个虎娃")
# else:
#     print('xiaokeai')

#定义字典
dict={}
for i in range(1,19):
    dict[i] = 0
print(dict)

a=[]
for i in range(1,11):
    if (i%2)==0:
        a.append(i*i)
print('a=',a)

#列表推导试
#数组
b=[i*i for i in range(1,11) if (i%2)==0]
print('b=',b)
#字典
xingzuo_name =('水瓶座','白羊座','双鱼座')
z={}
for i in xingzuo_name:
    z[i]=0
print(z)

y={i:0 for i in xingzuo_name}
print(y)
