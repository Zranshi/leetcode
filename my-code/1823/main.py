# -*- coding: UTF-8 -*-
# @Time     : 2021/08/19 07:44
# @Author   : Ranshi
# @File     : main.py


class Solution:

    def findTheWinner(self, n, k):
        if n == 1:
            return 1
        val = 0
        for i in range(2, n + 1):
            cur = (val + k) % i
            val = cur
        return val + 1


if __name__ == '__main__':
    print(Solution().findTheWinner(n=5, k=2))
