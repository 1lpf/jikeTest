import requests
class Common(object):
    def __init__(self,url_root):
        self.url_root = url_root
    def get(self,url,params=''):
        url = self.url_root + url + params
        res = requests.get(url)
        return res
    def post(self,url,params=''):
        url=self.url_root + url
        if len(params) > 0:
            res = requests.post(url,data=params)
        else:
            res = requests.post(url)
            return res

