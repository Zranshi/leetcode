#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/29 22:57
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 面试题 10.10. 数字流的秩
class StreamRank:
    def __init__(self):
        self.values = []

    def getIndex(self, x):
        i, j, n = 0, len(self.values), len(self.values)
        while i < j:
            m = (i + j) // 2
            if self.values[m] > x:
                j = m - 1
            else:
                i = m + 1
        return i if i >= n or self.values[i] > x else i + 1

    def track(self, x: int) -> None:
        if len(self.values) < 1:
            self.values.append(x)
        else:
            i = self.getIndex(x)
            self.values = self.values[:i] + [x] + self.values[i:]

    def getRankOfNumber(self, x: int) -> int:
        return self.getIndex(x)


if __name__ == "__main__":
    ...
