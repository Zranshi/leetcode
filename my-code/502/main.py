# -*- coding: UTF-8 -*-
# @Time     : 2021/09/09 18:05
# @Author   : Ranshi
# @File     : main.py


import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        lst = [(capital[i], profits[i]) for i in range(len(capital))]
        lst.sort(key=lambda x: x[0])
        idx = 0
        items = []
        heapq.heapify(items)
        for _ in range(k):
            while idx < len(capital) and lst[idx][0] <= w:
                heapq.heappush(items, -lst[idx][1])
                idx += 1

            if items:
                w -= heapq.heappop(items)
            else:
                break
        return w


if __name__ == "__main__":
    print(
        Solution().findMaximizedCapital(
            k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]
        )
    )
