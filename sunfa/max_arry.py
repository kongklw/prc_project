class MaxArry(object):

    def solution(self, arry):

        aim_list = []
        for length in range(len(arry), 0, -1):
            cursor = 0
            while cursor + length <= len(arry):
                new_arry = arry[cursor:cursor + length]
                print(new_arry)
                if len(set(new_arry)) == len(new_arry):
                    max_length = len(new_arry)
                    aim_list.append(new_arry)
                cursor += 1
            if len(aim_list) != 0:
                break

        return max_length, aim_list

    def child_arry(self, arry):
        print(arry)
        # 所有排列
        for item in arry:
            cursor = 0

        return None


if __name__ == '__main__':
    arry = [1, 5, 2, 4]
    maxarry = MaxArry()
    # res = maxarry.solution(arry)
    res = maxarry.child_arry(arry)

    print(res)
