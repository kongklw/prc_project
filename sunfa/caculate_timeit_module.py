def fa():
    alist = []

    for i in range(10):
        alist.append(i)
    # print(alist[:10])


def fb():
    alist = []
    for i in range(1000):
        alist.insert(-1, i)
    # print(alist[:10])


if __name__ == '__main__':
    # fa()
    # fb()
    import timeit

    #
    # print(timeit.timeit('fa()', setup='from __main__ import fa'))
    # print(timeit.timeit('fb()', setup='from __main__ import fb'))

    tfa = timeit.Timer('fa()', 'from __main__ import fa')

    print('fa时长', tfa.timeit(10000))

    tfb = timeit.Timer('fb()', 'from __main__ import fb')
    print('fb时长', tfb.timeit(10000))
