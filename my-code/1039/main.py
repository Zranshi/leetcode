# -*- coding:utf-8 -*-
# @Time     : 2021/5/27 21:02
# @Author   : Ranshi
# @File     : 1039. 多边形三角剖分的最低得分.py
from functools import lru_cache
from typing import List


class Solution:
    def minScoreTriangulation(self, a: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            res = 10000009
            for k in range(i + 1, j):
                res = min(res, dp(i, k) + dp(k, j) + a[i] * a[j] * a[k])
            return res % (10 ** 7 + 9)

        return dp(0, len(a) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.minScoreTriangulation([1, 2, 3]))
