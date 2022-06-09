# 记录12生肖，根据年份判断生肖
shengxiao = '鼠牛虎兔龙蛇马羊猴鸡狗猪'


#xingzuo_name =('水瓶座','白羊座','双鱼座')
#xingzuo_days =((1,20),(2,19),(3,21))

year = int(input('请输入出生年份'))
if(shengxiao[year%12])=='虎':
    print("是个虎娃")
else:
    print('xiaokeai')