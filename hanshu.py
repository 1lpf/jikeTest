#函数的定义和常用操作

# #读取任务名称
# f=open('name.txt',encoding='UTF-8')
# data = f.read()
# #split()拆分字符串。通过指定字符串对字符进行切片，并返回分割后的字符串列表（list）
# print(data.split('|'))

# #读取兵器名
# f1 = open('bingqi.txt',encoding='UTF-8')
# i=1
# for line in f1.readlines():
#     if i % 2 ==1:
# # strip()⽤于移除字符串头尾指定的字符（默认为空格）或字符序列。注意：该⽅法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#         print(line.strip('\n'))
#     i += 1

# #读取全文
# f2=open('sanguo.txt',encoding='UTF-8')
# #replace()替换函数
# data2=f2.read().replace('\n','')
# print(data2)

#-------------------------------------------
#函数
# def func(filename):
#     print(open(filename,encoding='UTF-8').read())
# func('name.txt')
# #查询人数在文章中出现的数量
# import re
# def find_item(hero):
#     with open('sanguo.txt',encoding='UTF-8') as f:
#         data = f.read().replace('\n','')
#         name_num=re.findall(hero,data)
#         print('主角 %s 出现 %s 次' %(hero,len(name_num)))
#     return len(name_num)
#
# ##读取任务信息
# name_dict={}
# with open('name.txt',encoding='UTF-8') as f:
#     for line in f:
#         names=line.split('|')
#         for n in names:
#             name_num=find_item(n)
#             name_dict[n]=name_num
#


#查询所需数据在文章中出现的个数
import re


def find_things(TH_name):
    with open('sanguo.txt',encoding='UTF-8') as f:
        data = f.read().replace('\n','')
        TH_num = re.findall(TH_name,data)
        print('%s 出现了 %s 次'%(TH_name,len(TH_num)))
    return TH_name,len(TH_num)

#获取人物信息
name_dict={}
with open('name.txt',encoding='UTF-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            peo_name,peo_num = find_things(n)
            name_dict[peo_name]=peo_num
#获取武器信息
wuqi_dict={}
with open('bingqi.txt',encoding='UTF-8') as f:
    i=1
    for line in f:
        if i%2==1:
            wuqi_name,wuqi_num = find_things(line.strip('\n'))
            wuqi_dict[wuqi_name]=wuqi_num
        i +=1