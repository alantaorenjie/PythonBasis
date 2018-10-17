# 装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2018-10-16')


print(now.__name__)
f = now
print(f.__name__)

print(now())


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('execute')
def now2():
    print('2015-10-17')


print(now2())

import time


def decorator(func):
    def wrapper(*args, **kw):
        start = time.time()
        f = func(*args, **kw)
        end = time.time()
        print('时间：', end - start)
    return wrapper


@decorator
def now3():
    time.sleep(0.2)


print(now3())
