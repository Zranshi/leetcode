# -*- coding: UTF-8 -*-
# @Time     : 2021/08/31 08:44
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(26):
            ch = chr(ord("a") + i)
            if s.count(ch) != t.count(ch):
                return False
        return True


if __name__ == "__main__":
    print(Solution().isAnagram(s="anagram", t="nagaram"))
