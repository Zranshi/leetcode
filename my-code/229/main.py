#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/22 08:03
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 229. 求众数 II
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}
        for v in nums:
            if v in cnt:
                cnt[v] += 1
            else:
                cnt[v] = 1
        return [item for item, value in cnt.items() if value > len(nums) // 3]


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))
