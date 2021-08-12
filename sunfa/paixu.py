class SortNum(object):

    def quick_sort(self, start, end, alist):
        if start >= end:
            return alist

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

        self.quick_sort(start, left_cursor, alist)
        self.quick_sort(right_cursor + 1, end, alist)

        return alist

    def bubble_sort(self, alist):

        for i in range(len(alist) - 1, 0, -1):
            for j in range(i):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
        return alist

    def fx(self):
        aim_list = []
        for i in range(1000):
            a = i
            for j in range(1000 - i):
                b = j
                c = 1000 - i - j
                head = (a ** 2) + (b ** 2)
                back = c ** 2
                if head == back:
                    print(head, back, a, b, c)
                    aim_list.append((a, b, c))

        return aim_list


if __name__ == '__main__':
    a = [3, 5, 6, 2, 4, 1, 2, 3, 5, 9, 0, 4, 5, 6, 1, 2, 8]
    sort_num = SortNum()
    # a = [3, 5, 6, 2, 4, 1]

    # 快排
    # start = 0
    # end = len(a) - 1
    # quick_res = sort_num.quick_sort(start, end, a)
    # print(quick_res)

    # 冒泡
    bubble_res = sort_num.bubble_sort(a)
    print(bubble_res)

    res = sort_num.fx()
    print(res)
