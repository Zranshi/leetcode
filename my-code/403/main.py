# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 403. 青蛙过河.py
import collections
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        set_stones = set(stones)
        dp = collections.defaultdict(set)
        dp[0] = {0}
        for stone in stones:
            for step in dp[stone]:
                for d in [-1, 0, 1]:
                    if step + d > 0 and stone + step + d in set_stones:
                        dp[stone + step + d].add(step + d)
        return len(dp[stones[-1]]) > 0


if __name__ == '__main__':
    s = Solution()
    print(s.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]))
