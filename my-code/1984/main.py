# -*- coding: UTF-8 -*-
# @Time     : 2022/02/11 04:51
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1984. 学生分数的最小差值
class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        res, left, right = float("inf"), 0, k - 1
        nums.sort()
        while right < len(nums):
            res = min(nums[right] - nums[left], res)
            right, left = right + 1, left + 1
        return res


if __name__ == "__main__":
    print(Solution().minimumDifference(nums=[9, 4, 1, 7], k=2))
