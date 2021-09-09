# -*- coding:utf-8 -*-
# @Time     : 2021/5/19 18:12
# @Author   : Ranshi
# @File     : 70. 爬楼梯.py
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n < 2:
            return 1
        res = 0
        for cur in range(1, n):
            res, a, b = a + b, b, a + b
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(4))
