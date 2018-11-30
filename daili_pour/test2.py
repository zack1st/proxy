import redis
from random import choice
from error import PoolEmptyError
from setting import *




class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        '''
        初始化
        :param host: Redis 地址
        :param post: Redis 端口
        :param password: Redis密码
        '''
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        print(self.db)
        print('连接成功')

    def add(self,proxy,score=INITIAL_SCORE):
        '''
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        '''
        #db.zscore返回成员key的分数，若成员元素不是有序集key的成员，或key不存在，返回nil。nil属于假
        if not self.db.zscore(REDIS_KEY1,proxy):
            print('in redis')
            print(proxy)
            print(type(proxy))
            #db.zadd将一个或多个成员元素及其分数值加入到有序集当中
            return self.db.zadd(REDIS_KEY1,{proxy:score})
        else:
            print('更新成功')
            return self.db.zadd(REDIS_KEY1,{proxy:score})

    def random(self):
        '''
        随机获取有效代理，首先尝试获取最高分代理，如果最高分不存在，则按照排名获取，否则异常
        :return: 随机代理
        '''
        result =  self.db.zrangebyscore(REDIS_KEY1,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            #0-100内递减排序
            result = self.db.zrevrange(REDIS_KEY1,0,100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError()

    def decrease(self,proxy):
        '''
        代理值减一分，分数小于最小值，则代理删除
        :param proxy: 代理
        :return: 修改后的代理分数
        '''
        score = self.db.zscore(REDIS_KEY1,proxy)
        if score and score > MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减1')
            #参数：key,score，value
            return self.db.zincrby(REDIS_KEY1,-1,proxy)
        else:
            print('代理',proxy,'当前分数',score,'移除')
            return self.db.zrem(REDIS_KEY1,proxy)

    def exists(self,proxy):
        '''
        判断是否存在
        :param proxy:代理
        :return: 是否存在
        '''
        return not self.db.zscore(REDIS_KEY1,proxy) == None

    def max(self,proxy):
        '''
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        '''
        print('代理',proxy,'可用，设置为',MAX_SCORE)
        return self.db.zadd(REDIS_KEY1,MAX_SCORE,proxy)

    def count(self):
        '''
        获取数量
        :return:数量
        '''
        return self.db.zcard(REDIS_KEY1)

    def all(self):
        '''
        获取所有代理
        :return: 全部代理列表
        '''
        return self.db.zrangebyscore(REDIS_KEY1,MIN_SCORE,MAX_SCORE)

    def batch(self,start,stop):
        '''
        批量湖区
        :param start:
        :param stop:
        :return: 代理列表
        '''
        return self.db.zrevrange(REDIS_KEY1,start,stop-1)

red = RedisClient()
red.add(proxy='123',score=12)

