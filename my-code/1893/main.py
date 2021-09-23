# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 10: 35
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set(range(left, right + 1))
        for item in ranges:
            for i in range(item[0], item[1] + 1):
                if i in s:
                    s.remove(i)
        return len(s) == 0


if __name__ == "__main__":
    print(
        Solution().isCovered(
            ranges=[[1, 2], [3, 4], [5, 6]],
            left=2,
            right=5,
        )
    )
