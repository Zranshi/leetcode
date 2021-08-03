# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 50
# @Author   : Ranshi
# @File     : 16. 最接近的三数之和.py
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, diff = float('inf'), float('inf')
        for i in range(0, len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[right] + nums[left]
                if abs(total - target) < diff:
                    res = total
                    diff = abs(total - target)
                if total == target:
                    return target
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest(nums=[2, 1, -4], target=1))
