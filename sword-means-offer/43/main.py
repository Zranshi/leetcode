#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/23 08:24
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 43. 1～n 整数中 1 出现的次数
class Solution:
    def countDigitOne(self, n: int) -> int:
        # mulk 表示 10^k
        # 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        # 但为了让代码看起来更加直观，这里保留了 k
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(
                max(n % (mulk * 10) - mulk + 1, 0), mulk
            )
            k += 1
            mulk *= 10
        return ans
