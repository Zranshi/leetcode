# -*- coding: UTF-8 -*-
# @Time     : 2023/02/13 21:30
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 083. 没有重复元素集合的全排列


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, combine = [], []
        mark = [False for _ in range(len(nums))]

        def dfs():
            if len(combine) == len(nums):
                res.append(combine[:])
                return
            for i in range(len(nums)):
                if not mark[i]:
                    mark[i] = True
                    combine.append(nums[i])
                    dfs()
                    combine.pop()
                    mark[i] = False

        dfs()
        return res


print(Solution().permute(nums=[1, 2, 3]))
