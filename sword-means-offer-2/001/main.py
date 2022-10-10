#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/12 19:08
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer II 001. 整数除法
class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        # 当被除数为最小值时, 除以-1可能会导致溢出
        if a == INT_MIN:
            if b == -1:
                return INT_MAX

        # 当除数为最小值的时候, 只有两种可能
        if b == INT_MIN:
            return 1 if a == INT_MIN else 0

        rev = False
        if a > 0:
            a = -a
            rev = not rev
        if b > 0:
            b = -b
            rev = not rev

        candidates = [b]

        while candidates[-1] >= a - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])

        ans = 0
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] >= a:
                ans += 1 << i
                a -= candidates[i]

        return -ans if rev else ans


if __name__ == "__main__":
    print(Solution().divide(15, 2))
