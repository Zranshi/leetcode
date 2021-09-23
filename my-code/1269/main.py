# -*- coding:utf-8 -*-
# @Time     : 2021/5/13 08:01
# @Author   : Ranshi
# @File     : 1269. 停在原地的方案数.py
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        max_column = min(arrLen - 1, steps // 2 + 1)

        dp = [0] * (max_column + 1)
        dp[0] = 1

        for i in range(1, steps + 1):
            dpNext = [0] * (max_column + 1)
            for j in range(0, max_column + 1):
                dpNext[j] = dp[j]
                if j - 1 >= 0:
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod
                if j + 1 <= max_column:
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext

        return dp[0]


if __name__ == "__main__":
    s = Solution()
    print(s.numWays(steps=4, arrLen=3))
