# -*- coding: UTF-8 -*-
# @Time     : 2021/09/14 07:15
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                return t
        return ""


if __name__ == "__main__":
    print(Solution().findLongestWord(s="abpcplea", dictionary=["ale", "apple", "monkey", "plea"]))
