#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/22 09:17
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 384. 打乱数组
import random


class Solution(object):
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> list[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> list[int]:
        shuffled = [0] * len(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums
