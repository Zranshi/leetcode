#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/09 08:32
# @Author   : Ranshi
# @File     : main.py
from typing import List
import random


class Solution:
    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, left, right):
        i = random.randint(left, right)
        nums[right], nums[i] = nums[i], nums[right]
        return self.partition(nums, left, right)

    def randomized_selected(self, arr, left, right, k):
        pos = self.randomized_partition(arr, left, right)
        num = pos - left + 1
        if k < num:
            self.randomized_selected(arr, left, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, right, k - num)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]


if __name__ == "__main__":
    print(Solution().getLeastNumbers(arr=[0, 1, 2, 1], k=1))
