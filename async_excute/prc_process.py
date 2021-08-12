from multiprocessing import Pool, Process
import os


def fx(n):
    return n * n


with Pool(5) as p:
    data = p.map(fx, [1, 2, 3])
    print(data)
print(data)

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    # f('bob')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
'''
main line
module name: __main__
parent process: 16398
process id: 14942
function f
module name: __main__
parent process: 14942
process id: 14956
hello bob

main line
module name: __main__
parent process: 16398
process id: 16544
function f
module name: __main__
parent process: 16398
process id: 16544
hello bob

'''

'''
进程管道技术
'''
# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()

'''
进程加锁
'''

from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
