#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/23 08:18
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 492. 构造矩形
import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        for i in range(int(math.sqrt(area)), 0, -1):
            if area % i == 0:
                return [area // i, i]


if __name__ == "__main__":
    print(Solution().constructRectangle(area=37))
