#redis数据库地址
REDIS_HOST = '127.0.0.1'

#redis端口
REDIS_PORT = 6379

#reids密码
REDIS_PASSWORD = 'zack'

REDIS_KEY = 'proxy'
REDIS_KEY1 = 'test'

#代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = False
API_ENABLED = False

# 最大批测试量
BATCH_TEST_SIZE = 10

#头部
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}