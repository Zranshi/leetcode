# -*- coding: UTF-8 -*-
# @Time     : 2023/02/13 21:29
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 082. 含有重复元素集合的组合


class Solution:
    def combinationSum2(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        if sum(candidates) < target:
            return []
        res, combine = set(), []

        def dfs(idx_target: int, idx):
            if idx_target == 0:
                res.add(tuple(sorted(combine)))
            if idx == len(candidates):
                return
            dfs(idx_target, idx + 1)
            if idx_target >= candidates[idx]:
                combine.append(candidates[idx])
                dfs(idx_target - candidates[idx], idx + 1)
                combine.pop()
            return

        dfs(target, 0)
        return list(res)


print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
