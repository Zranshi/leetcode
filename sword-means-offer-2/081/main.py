# -*- coding: UTF-8 -*-
# @Time     : 2023/02/05 17:20
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 081. 允许重复选择元素的组合
class Solution:
    def combinationSum(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        res = []
        idx_combine = []

        def dfs(idx_target: int, idx: int):
            if idx == len(candidates):
                return
            if idx_target == 0:
                res.append(idx_combine[:])
                return
            dfs(idx_target, idx + 1)
            if idx_target >= candidates[idx]:
                idx_combine.append(candidates[idx])
                dfs(idx_target - candidates[idx], idx)
                idx_combine.pop()
            return

        dfs(target, 0)
        return res


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
