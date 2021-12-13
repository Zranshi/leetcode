#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/12 19:28
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 002. 二进制加法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, sf = [], 0
        p_a, p_b = len(a) - 1, len(b) - 1

        while p_a >= 0 or p_b >= 0 or sf:
            idx = sf
            if p_a >= 0:
                idx += int(a[p_a])
                p_a -= 1
            if p_b >= 0:
                idx += int(b[p_b])
                p_b -= 1
            sf = 1 if idx >= 2 else 0
            res.append(str(idx % 2))

        return "".join(res[::-1])


if __name__ == "__main__":
    print(Solution().addBinary(a="1010", b="1011"))
