#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/15 10:08
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 319. 灯泡开关
from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n + 0.5))


if __name__ == "__main__":
    print(Solution().bulbSwitch())
