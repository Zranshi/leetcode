# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 10: 03
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def hanota(self, a: List[int], b: List[int], c: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        for x in a:
            c.append(x)


if __name__ == '__main__':
    s = Solution()
    print(s.hanota([2, 1, 0], [], []))
