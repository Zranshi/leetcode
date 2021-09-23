# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 07
# @Author   : Ranshi
# @File     : 321. 拼接最大数.py
from typing import List


class Solution:
    def maxNumber(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[int]:
        def getMaXArr(nums, i):
            if not i:
                return []
            stack, pop = [], len(nums) - i
            for num in nums:
                while pop and stack and stack[-1] < num:
                    pop -= 1
                    stack.pop()
                stack.append(num)
            return stack[:i]

        def merge(tmp1, tmp2):
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        return max(
            merge(getMaXArr(nums1, i), getMaXArr(nums2, k - i))
            for i in range(k + 1)
            if i <= len(nums1) and k - i <= len(nums2)
        )


if __name__ == "__main__":
    s = Solution()
    print(s.maxNumber(nums1=[3, 4, 6, 5], nums2=[9, 1, 2, 5, 8, 3], k=5))
