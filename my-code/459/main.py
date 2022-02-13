# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 22:28
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(2, len(s) + 1):
            idx_str = s[: len(s) // i] * i
            if idx_str == s:
                return True
        return False


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))
