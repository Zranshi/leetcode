# -*- coding: UTF-8 -*-
# @Time     : 2021/09/27 08:51
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def firstUniqChar(self, s: str) -> str:
        ch_set = {}
        for ch in s:
            if ch not in ch_set:
                ch_set[ch] = 1
            else:
                ch_set[ch] += 1
        for key in ch_set:
            if ch_set[key] == 1:
                return key
        return " "


if __name__ == "__main__":
    print(Solution().firstUniqChar(s="abaccdeff"))
