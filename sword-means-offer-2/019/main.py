# -*- coding: UTF-8 -*-
# @Time     : 2022/09/12 16:52
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 019. 最多删除一个字符得到回文
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low: int, high: int):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low, high = low + 1, high - 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True


if __name__ == "__main__":
    print(Solution().validPalindrome(s="aba"))
