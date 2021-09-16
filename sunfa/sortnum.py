def maopao(alist):
    for i in range(len(alist) - 1, 0, -1):

        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    return alist


# 19分
def quick_sort(start, end, alist):
    if start >= end:
        return

    left_cursor = start
    right_cursor = end

    mid = alist[left_cursor]

    while left_cursor < right_cursor:

        while left_cursor < right_cursor and alist[right_cursor] >= mid:
            right_cursor -= 1
        alist[left_cursor], alist[right_cursor] = alist[right_cursor], alist[left_cursor]

        while left_cursor < right_cursor and alist[left_cursor] <= mid:
            left_cursor += 1
        alist[left_cursor], alist[right_cursor] = alist[right_cursor], alist[left_cursor]

    quick_sort(start, left_cursor, alist)
    quick_sort(right_cursor + 1, end, alist)

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
    alist = [3, 2, 1, 5, 4, 0, 9, 2, 3, 7, 5]

    # blist = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    # twodiv(blist, 5)
    mp_res = maopao(alist)
    print(mp_res)

    start = 0
    end = len(alist) - 1
    qs_res = quick_sort(start, end, alist)
    print(qs_res)
