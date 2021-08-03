# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 132. 分割回文串 II.py
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        res = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                res[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        res[i] = min(res[i], res[j] + 1)
        return int(res[n - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.minCut(s="aab"))
