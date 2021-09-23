# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 633. 平方数之和.py
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        index = 0
        while index ** 2 <= c:
            f = math.sqrt(c - index ** 2)
            if f == int(f):
                return True
            index += 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum(c=6))
