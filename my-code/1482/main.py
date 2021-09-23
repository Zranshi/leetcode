# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18:21
# @Author   : Ranshi
# @File     : 1482. 制作 m 束花所需的最少天数.py
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def check(day: int) -> bool:
            bouquets = flowers = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        if bouquets == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquets == m

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    s = Solution()
    print(s.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
