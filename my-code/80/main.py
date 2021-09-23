# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 56
# @Author   : Ranshi
# @File     : 80. 删除有序数组中的重复项 II.py
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 2
        idx = 0
        if len(nums) < 3:
            return len(nums)
        for i in range(2, len(nums)):
            if (
                nums[i - 1 - idx] == nums[i - 2 - idx]
                and nums[i] == nums[i - 1 - idx]
            ):
                idx += 1
            else:
                nums[i - idx] = nums[i]
                length += 1
            print(nums)
        return length


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
