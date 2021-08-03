# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 00:27
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s))
    print(s)
