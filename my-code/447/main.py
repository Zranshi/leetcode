# -*- coding: UTF-8 -*-
# @Time     : 2021/09/13 07:19
# @Author   : Ranshi
# @File     : main.py
from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            cnt = defaultdict(int)
            for q in points:
                dis = (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])
                cnt[dis] += 1
            for m in cnt.values():
                ans += m * (m - 1)
        return ans


if __name__ == "__main__":
    print(Solution().numberOfBoomerangs(points=[[0, 0], [1, 0], [2, 0]]))
