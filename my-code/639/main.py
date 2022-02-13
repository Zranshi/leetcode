# -*- coding: UTF-8 -*-
# @Time     : 2021/09/27 00:00
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        if s[0] == "0":
            dp[1] = 0
        elif s[0] == "*":
            dp[1] = 9
        else:
            dp[1] = 1

        for i in range(1, n):
            if s[i] == "*":
                # ----单独作为一个数字
                dp[i + 1] = dp[i] * 9  # "*"作为单独一个数字
                # ----与前一位配合，组建2位数
                if s[i - 1] == "1":
                    dp[i + 1] += dp[i - 1] * 9  # 与前面的1联合
                elif s[i - 1] == "2":
                    dp[i + 1] += dp[i - 1] * 6  # 与前面的2联合
                elif s[i - 1] == "*":
                    dp[i + 1] += dp[i - 1] * 15  # 前面的'*'可以当1，可以当2
                dp[i + 1] %= MOD
            else:
                # ----单独作为一个数字
                dp[i + 1] = dp[i] if s[i] != "0" else 0
                # ----与前一位配合，组建2位数
                if s[i - 1] == "1":  # 与前面的1联合
                    dp[i + 1] += dp[i - 1]
                elif s[i - 1] == "2":  # 与前面的2联合
                    if int(s[i], 10) <= 6:
                        dp[i + 1] += dp[i - 1]
                elif s[i - 1] == "*":
                    dp[i + 1] += dp[i - 1]
                    if int(s[i], 10) <= 6:
                        dp[i + 1] += dp[i - 1]
                dp[i + 1] %= MOD
        return dp[n]


if __name__ == "__main__":
    print(Solution().numDecodings(s="*"))
