class PoolEmptyError(Exception):
    def __init__(self):
        Exception.__init__(self)
    #__str__将实例变成字符串
    def __str__(self):
        return repr('代理池已经枯竭')











