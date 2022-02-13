#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/26 08:00
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 496. 下一个更大元素 I
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]
