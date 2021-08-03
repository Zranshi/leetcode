# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 02
# @Author   : Ranshi
# @File     : 189. 旋转数组.py
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
