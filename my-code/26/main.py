# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 50
# @Author   : Ranshi
# @File     : 26. 删除有序数组中的重复项.py
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        if len(nums) < 2:
            return len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1 - index]:
                index += 1
            else:
                nums[i - index] = nums[i]
        return len(nums) - index


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums=[1, 1, 2]))
