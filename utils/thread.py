from threading import Thread
from functools import wraps


'''
# 定义线程异步执行的装饰器

导包方法：from utils.thread import AsyncThread
使用方法：函数前添加@Async注解 
'''
def AsyncThread(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper
