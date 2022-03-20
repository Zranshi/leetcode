# -*- coding: UTF-8 -*-
# @Time     : 2022/03/13 14:17
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 798. 得分最高的最小轮调
class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx


print(Solution().bestRotation(nums=[4, 1, 4, 0, 0]))