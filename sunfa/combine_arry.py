import time


def fx(a, b):
    time.sleep(1)
    aim_list = []
    a_length = len(a)
    b_length = len(b)
    a_cursor = 0
    b_cursor = 0

    for i in range(a_length + b_length):
        if a_cursor == a_length:
            aim_list += b[b_cursor:]
            break
        elif b_cursor == b_length:
            aim_list += a[a_cursor:]
            break
        else:
            if a[a_cursor] < b[b_cursor]:
                aim_list.append(a[a_cursor])
                a_cursor += 1
            else:
                aim_list.append(b[b_cursor])
                b_cursor += 1

    return aim_list


def fx2(a, b):
    time.sleep(1)
    c = a + b
    # c = sorted(c)
    c.sort()
    return c


def fx3(a, b):
    time.sleep(1)
    res = []
    while a or b:
        if not a:
            res.extend(b)
            return res
        elif not b:
            res.extend(a)
            return res
        else:
            res.append(a.pop(0) if a[0] <= b[0] else b.pop(0))


def merge_sort(nums1, nums2):
    time.sleep(1)
    m = []
    i, j = 0, 0
    l_1, l_2 = len(nums1) - 1, len(nums2) - 1
    # 当i，j的索引位置小于等于索引最大值的时候
    while i <= l_1 and j <= l_2:
        if nums1[i] <= nums2[j]:
            m.append(nums1[i])
            i += 1
        else:
            m.append(nums2[j])
            j += 1
    m = m + nums1[i:] + nums2[j:]
    return m


if __name__ == '__main__':
    a = [1] * 50 + [2] * 100 + [3] * 1000 + [4] * 20 + [5] * 10 + [6] * 20
    b = [2] * 30 + [4] * 100 + [6] * 100 + [8] * 100 + [9] * 100

    ts2 = time.time()
    res2 = fx2(a, b)
    td2 = time.time()
    print('方式2耗时', td2 - ts2)
    # print(res2)

    ts4 = time.time()
    res4 = merge_sort(a, b)
    td4 = time.time()
    print('方式4耗时', td4 - ts4)
    # print(res3)

    ts = time.time()
    res = fx(a, b)
    t1 = time.time()
    print('方式1耗时', t1 - ts)
    # print(res)

    ts3 = time.time()
    res3 = fx3(a, b)
    td3 = time.time()
    print('方式3耗时', td3 - ts3)
    # print(res3)

    aim = [1, 4, 2, 1, 3]
    aim.sort()

    blist = [1, 2, 6, 4, 2, 3, 1]
    clist = sorted(blist)
    print(aim)
    print(clist)
    if (td3 - ts3) > (t1 - ts):
        print('算法时间长')
