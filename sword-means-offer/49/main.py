#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 11:52
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 49. 丑数
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for _ in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


if __name__ == "__main__":
    print(Solution().nthUglyNumber(n=10))
