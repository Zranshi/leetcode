# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 00:27
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s))
    print(s)
