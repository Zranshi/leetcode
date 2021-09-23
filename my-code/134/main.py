# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 134. 加油站.py
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        a = []
        for i in range(len(gas)):
            a.append(gas[i] - cost[i])
        if sum(a) < 0:
            return -1
        start, money = 0, 0
        for i in range(len(a)):
            money += a[i]
            if money < 0:
                start = i + 1
                money = 0
        return start


if __name__ == "__main__":
    s = Solution()
    a = input()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
