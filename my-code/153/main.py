# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 153. 寻找旋转排序数组中的最小值.py
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        pre = nums[0]
        for x in nums:
            if x < pre:
                return x
            if pre > x:
                pre = x
        return pre


if __name__ == '__main__':
    s = Solution()
    print(s.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
