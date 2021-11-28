#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/27 08:20
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 519. 随机翻转矩阵
import random


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> list[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        # 查找位置 x 对应的映射
        idx = self.map.get(x, x)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()


if __name__ == "__main__":
    s = Solution(3, 1)
    print(s.flip())
    print(s.flip())
    print(s.flip())
    s.reset()
    print(s.flip())
