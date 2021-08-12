def maopao(alist):
    for j in range(len(alist) - 1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    return alist


def quick_sort(alist):
    start = 0
    end = len(alist) - 1

    if start >= end:
        return

    mid = alist[start]

    left_cursor = start
    right_cursor = end

    while left_cursor < right_cursor:

        while left_cursor < right_cursor and alist[right_cursor] > mid:
            right_cursor -= 1
        alist[left_cursor], alist[right_cursor] = alist[right_cursor], alist[left_cursor]

        while left_cursor < right_cursor and alist[left_cursor] < mid:
            left_cursor += 1
        alist[left_cursor], alist[right_cursor] = alist[right_cursor], alist[left_cursor]

    quick_sort(alist[:left_cursor])
    quick_sort(alist[right_cursor:])

    return alist


def twodiv(blist, n):
    length = len(blist)
    index = int(length / 2)
    count = blist[index]

    if count == n:
        print('has data')
    elif count > n and length != 1:
        twodiv(blist[:index], n)
    elif count < n and length != 1:
        twodiv(blist[index:], n)
    else:
        print('no data')


if __name__ == '__main__':
    alist = [3, 2, 1, 5, 4, 0]

    # blist = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    # twodiv(blist, 5)
    # mp_res = maopao(alist)
    # print(mp_res)

    qs_res = quick_sort(alist=[3, 5, 1, 2, 4, 0])
    print(qs_res)
