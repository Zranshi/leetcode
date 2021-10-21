#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 11:51
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 19. 正则表达式匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == "*":
                    if dp[i][j - 2]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True  # 2.
                    elif dp[i - 1][j] and p[j - 2] == ".":
                        dp[i][j] = True  # 3.
                elif dp[i - 1][j - 1]:
                    if s[i - 1] == p[j - 1]:
                        dp[i][j] = True  # 1.
                    elif p[j - 1] == ".":
                        dp[i][j] = True  # 2.
        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().isMatch(s="aa", p="a"))
