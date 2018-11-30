
from db import RedisClient
from crawler import Crawler


from setting import *

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        '''
        判断是否达到了代理池限制
        :return:
        '''
        if self.redis.count() > POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        '''
        开始执行
        :return:
        '''
        print('获取器开始执行')
        if not self.is_over_threshold():
            print('1')
            #获取代理池的代理总数
            # #__CrawlFunc__是列表，存放获取代理网函数的名称
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                print('2')
                #callback就是crawl类里面的属性函数名称
                callback = self.crawler.__CrawlFunc__[callback_label]
                print('3')
                proxies = self.crawler.get_proxies(callback)
                print('4')
                for proxy in proxies:
                    print('5')
                    self.redis.add(proxy)






