#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/09 08:43
# @Author   : Ranshi
# @File     : main.py
import heapq


class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heapq.heappush(self.B, -heapq.heappushpop(self.A, num))
        else:
            heapq.heappush(self.A, -heapq.heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return (
            self.A[0]
            if len(self.A) != len(self.B)
            else (self.A[0] - self.B[0]) / 2.0
        )
