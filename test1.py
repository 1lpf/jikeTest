
# Python代码中引入requests库，引入后才可以在你的代码中使用对应的类以及成员函数
import requests
# 建立url_index的变量，存储战场的首页
#url_index='https://passport.baidu.com/v2/api/?login'
# 调用requests类的get方法，也就是HTTP的GET请求方式，访问了url_index存储的首页URL，返回结果存到了response_index中
#response_index = requests.get(url_index)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
#print('Response内容：'+response_index.text)

from commom import Common
url = '/'
comm=Common()
response_index=comm.get(url)
print('Response内容：'+response_index.text)