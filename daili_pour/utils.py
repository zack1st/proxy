
import requests
from requests.exceptions import ConnectionError

base_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

#当options字典有新的要求添加的时候，dict(base_headers,**options)可以将条件按照headers的要求添加进headers
def get_page(url,options={}):
    '''
    抓取代理
    :param url:
    :param options:新添加进headers的条件
    :return:抓取的文本
    '''
    headers = dict(base_headers,**options)
    print('正在抓取',url)
    try:
        response = requests.get(url=url,headers=headers)
        print('抓取成功',url,response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取失败',url)
        return None





