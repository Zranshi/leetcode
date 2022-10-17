# -*- coding: UTF-8 -*-
# @Time     : 2022/10/16 01:17
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 065. 最短的单词编码
class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)


print(Solution().minimumLengthEncoding(words=["time", "me", "bell"]))
