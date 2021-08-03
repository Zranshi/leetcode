# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 62. 不同路径.py
class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1)] * (m - 1)
        for x in dp:
            print(x)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for x in dp:
            print(x)
        return dp[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return math.comb(m + n - 2, n - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(m=3, n=7))
