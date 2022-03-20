# -*- coding: UTF-8 -*-
# @Time     : 2022/03/04 09:42
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 2104. 子数组范围和
class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        min_left, max_left = [0] * n, [0] * n
        min_stack, max_stack = [], []
        for i, v in enumerate(nums):
            while min_stack and nums[min_stack[-1]] > v:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] <= v:
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)

        minRight, maxRight = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        sumMax, sumMin = 0, 0
        for i, num in enumerate(nums):
            sumMax += (maxRight[i] - i) * (i - max_left[i]) * num
            sumMin += (minRight[i] - i) * (i - min_left[i]) * num
        return sumMax - sumMin


print(Solution().subArrayRanges(nums=[1, 2, 3]))
