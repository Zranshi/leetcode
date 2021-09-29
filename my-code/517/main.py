# -*- coding: UTF-8 -*-
# @Time     : 2021/09/29 08:37
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def findMinMoves(self, a: List[int]) -> int:
        if sum(a) % len(a) != 0:
            return -1
        avg: int = sum(a) // len(a)
        ans = s = 0
        for i in a:
            s += i - avg
            ans = max(ans, abs(s), i - avg)

        return ans


if __name__ == "__main__":
    print(Solution().findMinMoves(a=[1, 0, 5]))
