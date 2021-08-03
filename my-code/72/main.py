# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 72. 编辑距离.py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if len1 * len2 == 0:
            return len1 + len2
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for i in range(len2 + 1):
            dp[0][i] = i
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)
        for i in range(0, len1):
            for j in range(0, len2):
                print(dp[i][j], end=" ")
            print()
        return dp[len1][len2]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance(word1="intention", word2="execution"))
