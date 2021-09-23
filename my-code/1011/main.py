# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 1011. 在 D 天内送达包裹的能力.py
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)

        def check(ans: int) -> int:
            day, index = 1, 0
            for item in weights:
                index += item
                if index > ans:
                    index = item
                    day += 1

            return day

        while left <= right:
            mid = (left + right) // 2
            day = check(mid)
            if day > D:
                left = mid + 1
            elif day <= D:
                right = mid - 1
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.shipWithinDays(weights=[1, 2, 3, 1, 1], D=4))
