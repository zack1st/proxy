
from utils import get_page
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(cls,name,bases,attrs):
        count = 0
        #attrs是属性集，此集可以被继承当次类被继承时候，继承为属性
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        #创建新的对象
        return type.__new__(cls,name,bases,attrs)

class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        '''
        将所有以crawl_开头的函数执行一遍，每次执行返回一个代理，并且将代理存进列表
        :param callback: 函数名字
        :return: 执行所有函数后返回的代理列表
        '''
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies


    # def crawl_daili66(self,page_count=4):
    #     '''
    #     获取代理66
    #     :param page_count: 页码
    #     :return: 代理
    #     '''
    #     start_url = 'http://www.66ip.cn/{}.html'
    #     # urls = [start_url.format(page) for page in range(1,page_count+1)]
    #     # for url in urls:
    #     #     print('Crawl',url)
    #     #     html = get_page(url)
    #     #     if html:
    #     #         doc = pq(html)
    #     #         trs = doc('.containerbox table tr:gt(0)').items()
    #     #         for tr in trs:
    #     #             ip = tr.find('td:nth-child(1)').text()
    #     #             port = tr.find('td:nth-child(2)').text()
    #     #             yield ':'.join([ip,port])

    def crawl_data5u(self):
        start_url = 'http://www.data5u.com/free/index.html'
        print('Crawl',start_url)
        html = get_page(start_url)
        if html:
            doc = pq(html)
            li_list = doc('.wlist li .l2').items()
            for li in li_list:
                doc1 = pq(li)
                text = doc1('li').text()
                list = text.split(' ')
                ip = list[0]
                port = list[1]
                yield ':'.join([ip,port])











