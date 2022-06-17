#捕获异常

#
# NameError---a = b 变量未定义
# SyntaxError---语法错误
# IndexError----超出索引范围
# KeyError----字典中key不存在
# ValueError
# AttributeError---属性错误
# TypeError

# #NameError
# try:
#     a = b
# except NameError:
#     print('NameError：变量未定义')
#
# #KeyError
# try:
#     dict = {'a':'aa','b':'bb'}
#     print(dict['c'])
# except KeyError:
#     print('KeyError：查询的值不存在')
#
#
# #ValueError
# #原始语句
# year = int(input('input year:'))
# #捕获异常
# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字')
#
#
# # #AttributeError
# try:
#     a=124
#     a.append()
# except AttributeError:
#     print('int类型不能增加')

# #提示原有的报错信息
# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print('0不能做除数 %s' %e)

# #捕获所有异常
# try:
#     print(1 / 'a')
# except Exception as e:
#     print('%s' %e)

# #自定义错误信息raise关键字
#
# try:
#      year = int(input('input year:'))
#      raise ValueError("输入的年份year 必须是数字")
# except ValueError as e:
#      print("引发异常：", repr(e))
# #----------------
# try:
#     a = input("输入一个数：")
#     #判断用户输入的是否为数字
#     if(not a.isdigit()):
#         raise ValueError("输入 必须是数字")
# except ValueError as e:
#     print("引发异常：",repr(e))

#finall有异常后也会执行的操作
try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()