# -*- coding: UTF-8 -*-
# @Time     : 2022/03/08 08:38
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 2055. 蜡烛之间的盘子
class Solution:
    def platesBetweenCandles(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, idx = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == "*":
                sum += 1
            else:
                idx = i
            preSum[i] = sum
            left[i] = idx

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if 0 <= x < y and y >= 0:
                ans[i] = preSum[y] - preSum[x]
        return ans


print(
    Solution().platesBetweenCandles(
        s="***|**|*****|**||**|*",
        queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]],
    )
)
