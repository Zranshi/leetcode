# -*- coding: UTF-8 -*-
# @Time     : 2021/08/27 06:46
# @Author   : Ranshi
# @File     : 123.py
import heapq


class MedianFinder:
    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        if not self.min or num <= -self.min[0]:
            heapq.heappush(self.min, -num)
            if len(self.max) + 1 < len(self.min):
                heapq.heappush(self.max, -heapq.heappop(self.min))
        else:
            heapq.heappush(self.max, num)
            if len(self.max) > len(self.min):
                heapq.heappush(self.min, -heapq.heappop(self.max))

    def findMedian(self) -> float:
        if len(self.min) > len(self.max):
            return -self.min[0]
        return (-self.min[0] + self.max[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    for i in range(1, 100, 10):
        mf.addNum(i)
    print(mf.findMedian())
