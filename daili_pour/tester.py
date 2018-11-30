from db import RedisClient
import aiohttp
import asyncio
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError

from setting import *

class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self,proxy):
        '''
        测试单个代理
        :param proxy:
        :return: None
        '''
        #连接
        # 创建aiohttp的ClientSession对象，类似requests的session对象
        async with aiohttp.ClientSession() as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试',proxy)
                async with session.get(TEST_URL,proxy=real_proxy,verify_ssl=False,timeout=60,allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法',proxy)
            except (ClientError, aiohttp.client_exceptions.ClientProxyConnectionError, asyncio.TimeoutError, AttributeError) as e:
                print(e.args)
                self.redis.decrease(proxy)
                print('代理请求失败',proxy)

    def run(self):
        '''
        测试主函数
        :param self:
        :return: None
        '''
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', stop, '个代理')
                test_proxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                '''对指定数量内的代理进行测试'''
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                # 输出刷新 每次返回一点
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试台发生错误', e.args)





















