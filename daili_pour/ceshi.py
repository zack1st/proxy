# import requests
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# }
#
# proxy = {
#     'http':'195.209.176.2:8893'
# }
#
# url = 'https://www.baidu.com'
#
# res = requests.get(url=url,headers=headers,proxies=proxy)
#
# print(res.status_code)
# import aiohttp
#
#
# TEST_URL = 'https://www.baidu.com'
# proxy = '41.33.15.50:8487'
# conn = aiohttp.TCPConnector(verify_ssl=False)
#
# async with aiohttp.ClientSession(connector=conn) as session:
#     try:
#         real_proxy = 'http://' + proxy
#         print('正在测试', proxy)
#         with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
#             if response.status in [200]:
#                 print('代理可用', proxy)
#             else:
#                 print('请求响应码不合法', proxy)
#     except :
#         print('代理请求失败', proxy)

# import aiohttp
# import asyncio
#
# async def get_text():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.baidu.com',timeout=20,allow_redirects=False) as resp:
#             print(resp.status)
#
# loop = asyncio.get_event_loop()
# tasks = get_text()
# loop.run_until_complete(asyncio.wait(tasks))

# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#
import asyncio
import aiohttp
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError

#
# # async def main():
# #     async with aiohttp.ClientSession() as session:
# #         async with session.get('https://api.github.com/events') as resp:
# #             print(resp.status)
# #             print(await resp.text())
# #
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())
#
semaphore = asyncio.Semaphore(2)
async def get_text():
    try:
        async with semaphore:
            async with aiohttp.ClientSession() as session:

                proxy = 'http://183.6.120.29:1080'
                async with session.get('https://www.baidu.com',proxy=proxy,verify_ssl=False,timeout=60,allow_redirects=False) as resp:
                    if resp.status == 200:
                        print('useful')
                        #print(resp.text())
    except Exception as e:
        print(e.args)

loop = asyncio.get_event_loop()
task = [get_text() for i in range(4)]
loop.run_until_complete(asyncio.wait(task))
loop.close()

# conn = aiohttp.TCPConnector(verify_ssl=False)
# print(conn)
# async def test_single_proxy(proxy):
#     async with aiohttp.ClientSession(connector=conn) as session:
#         # try:
#         #     print('succeed')
#         # except (ClientError, aiohttp.client_exceptions.ClientProxyConnectionError, asyncio.TimeoutError, AttributeError):
#         #     print('false')
#         try:
#             if isinstance(proxy, bytes):
#                 proxy = proxy.decode('utf-8')
#             real_proxy = 'http://' + proxy
#             print('正在测试', proxy)
#             async with session.get('https://www.baidu.com', proxy=real_proxy, timeout=15, allow_redirects=False) as response:
#                 if response.status in [200]:
#                     print('代理可用', proxy)
#                 else:
#                     print('请求响应码不合法', proxy)
#         except (ClientError, aiohttp.client_exceptions.ClientProxyConnectionError, asyncio.TimeoutError, AttributeError):
#             print('代理请求失败', proxy)
#
# if __name__ == '__main__':
#     proxy = '98.172.142.174:8319'
#     loop = asyncio.get_event_loop()
#     tasks = [test_single_proxy(proxy)]
#     loop.run_until_complete(asyncio.wait(tasks))















