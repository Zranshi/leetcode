# -*- coding: UTF-8 -*-
# @Time     : 2021/08/26 20:28
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        lst, res = [], []

        def dfs(idx_num: int, idx: int):
            if idx_num == target:
                res.append(lst[:])
            else:
                for i in range(idx, len(candidates)):
                    if candidates[i] <= target - idx_num:
                        lst.append(candidates[i])
                        dfs(idx_num + candidates[i], i)
                        lst.pop()
                    else:
                        break

        dfs(0, 0)
        return res


if __name__ == "__main__":
    print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
