# coding: utf-8
# @Time     : 2021/08/12 08:04
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == "__main__":
    print(Solution().longestPalindromeSubseq(s="bbbab"))
