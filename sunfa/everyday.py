class EveryDady(object):

    def max_palindrome(self, s):
        '''
        给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
        子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

        输入：s = "bbbab"
        输出：4
        解释：一个可能的最长回文子序列为 "bbbb" 。

        输入：s = "cbbd"
        输出：2
        解释：一个可能的最长回文子序列为 "bb" 。


        :param s: 字符串
        :return: 最长回文长度
        '''
        # 字符串切片，然后判断回文。

        # 情况 ，最大回文，位置不固定。回文最长整个数组的长度.

        # 字符串子串
        for i in range(len(s)):
            pass

        return None

    def num_count(self, num, n):
        # 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

        # simple method 1
        count = 0
        for i in range(n + 1):
            single_count = str(i).count(str(num))
            count += single_count

        # method 2 把数值为1 的从小到大


        return count


if __name__ == '__main__':
    ed = EveryDady()

    s = "bbbab"
    # print(s.count('b'))
    # max_palindrome = ed.max_palindrome(s)
    # print(max_palindrome)

    num_count = ed.num_count(1, 0)
    print(num_count)
