# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 628. 三个数的最大乘积.py
from typing import List


class Solution:
    def maximumProduct1(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)

    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = float("-inf")
        d = e = float("inf")
        for i, num in enumerate(nums):
            # 更新最大三个数
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
            # 更新最小两个数
            if num < d:
                d, e = num, d
            elif num < e:
                e = num
        return max(d * e * a, a * b * c)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumProduct([1, 2, 3, 4]))
