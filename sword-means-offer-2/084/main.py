# -*- coding: UTF-8 -*-
# @Time     : 2023/02/13 21:31
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 084. 含有重复元素集合的全排列


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res, combine = set(), []
        mark = [False for _ in range(len(nums))]

        def dfs():
            if len(combine) == len(nums):
                res.add(tuple(combine))
                return
            for i in range(len(nums)):
                if not mark[i]:
                    mark[i] = True
                    combine.append(nums[i])
                    dfs()
                    combine.pop()
                    mark[i] = False

        dfs()
        return list(res)


print(Solution().permuteUnique(nums=[1, 1, 2]))
