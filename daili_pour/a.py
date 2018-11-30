
from selenium import webdriver
import requests
from pyquery import PyQuery as pq


#browser = webdriver.Chrome(r'C:\Program Files\chromedriver\chromedriver.exe')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
url = 'http://www.data5u.com/free/index.html'

res = requests.get(url=url,headers=headers)
html = res.text
doc = pq(html)
li_list = doc('.wlist li .l2').items()
for li in li_list:
    # print(li)
    # print('============')
    doc1 = pq(li)
    text = doc1('li').text()
    list = text.split(' ')
    ip = list[0]
    port = list[1]
    ip_port = ip + ':' + port
    print(ip_port)















