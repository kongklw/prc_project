from concurrent.futures.thread import ThreadPoolExecutor
import time


def pow(a, b):
    return a + b


#
# with ThreadPoolExecutor(max_workers=10) as executor:
#     future = executor.submit(pow, 323, 1235)
#     print(future.result())

'''
a的结果等待b的结果出来
b的结果等待a的结果出来 
产生死锁
'''

# def wait_on_b():
#     time.sleep(5)
#     print(b.result())  # b will never complete because it is waiting on a.
#     return 5
#
#
# def wait_on_a():
#     time.sleep(6)
#     print(a.result())  # a will never complete because it is waiting on b.
#     return 6
#
#
# executor = ThreadPoolExecutor(max_workers=2)
# a = executor.submit(wait_on_b)
# b = executor.submit(wait_on_a)

"""
线程死锁的情况是
线程池只开启一个线程，调用了主函数wait_on_future 执行，那么pow就不会执行，不会有结果。
"""
# def wait_on_future():
#     f = executor.submit(pow, 5, 2)
#     # This will never complete because there is only one worker thread and
#     # it is executing this function.
#     print(f.result())
#
#
# executor = ThreadPoolExecutor(max_workers=2)
# a = executor.submit(wait_on_future)
# print('a result', a.result())


import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 3): url for url in URLS}
    print(future_to_url)
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

'''
ProcessPoolExecutor
进程实例
'''
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()
