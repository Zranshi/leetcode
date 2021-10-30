#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/28 07:58
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 重新排序得到 2 的幂
from typing import Tuple


def countDigits(n: int) -> Tuple[int]:
    cnt = [0] * 10
    while n:
        cnt[n % 10] += 1
        n //= 10
    return tuple(cnt)


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_digits = {countDigits(1 << i) for i in range(30)}

        return countDigits(n) in power_of_digits


if __name__ == "__main__":
    print(Solution().reorderedPowerOf2(46))
