# -*- coding: UTF-8 -*-
# @Time     : 2021/08/15 08:12
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def findPaths(
        self, m: int, n: int, max_move: int, start_row: int, start_col: int
    ) -> int:
        MOD = 10 ** 9 + 7

        outCounts = 0
        dp = [[0] * n for _ in range(m)]
        dp[start_row][start_col] = 1
        for i in range(max_move):
            dpNew = [[0] * n for _ in range(m)]
            for j in range(m):
                for k in range(n):
                    if dp[j][k] > 0:
                        for j1, k1 in [
                            (j - 1, k),
                            (j + 1, k),
                            (j, k - 1),
                            (j, k + 1),
                        ]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dpNew[j1][k1] = (dpNew[j1][k1] + dp[j][k]) % MOD
                            else:
                                outCounts = (outCounts + dp[j][k]) % MOD
            dp = dpNew

        return outCounts


if __name__ == "__main__":
    print(Solution().findPaths(m=2, n=2, max_move=2, start_row=0, start_col=0))
