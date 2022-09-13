# -*- coding: UTF-8 -*-
# @Time     : 2022/09/13 17:12
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 020. 回文子字符串的个数


class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(2 * n + 1):
            left, right = i // 2, i // 2 + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left, right = left - 1, right + 1
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().countSubstrings(s="aaa"))
