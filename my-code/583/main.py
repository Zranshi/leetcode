# -*- coding: UTF-8 -*-
# @Time     : 2021/09/25 06:59
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[len1][len2]
        return len1 - lcs + len2 - lcs


if __name__ == "__main__":
    print(Solution().minDistance("sea", "eat"))
