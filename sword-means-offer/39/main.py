#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/15 08:05
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 39. 数组中出现次数超过一半的数字
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
