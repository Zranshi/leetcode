# -*- coding: UTF-8 -*-
# @Time     : 2022/11/12 20:22
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 071. 按权重生成随机数
import bisect
from random import random


class Solution:
    def __init__(self, w: list[int]):
        self.check_table = []
        sum = 0
        for v in w:
            sum += v
            self.check_table.append(sum)
        self.total = sum

    def pickIndex(self) -> int:
        num = random() * self.total
        return bisect.bisect_left(self.check_table, num)


print(Solution([1, 3]).pickIndex())
