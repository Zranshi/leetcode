#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/08 17:01
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 598. 范围求和 II
class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb


if __name__ == "__main__":
    print(Solution().maxCount(m=3, n=3, operations=[[2, 2], [3, 3]]))
