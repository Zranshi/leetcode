# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 22
# @Author   : Ranshi
# @File     : 1723. 完成所有工作的最短时间.py
from typing import List


# def backtrace(jobs: List[int], group: List[int], n: int) -> bool:
#     """回溯函数

#     Args:
#         jobs (List[int]): 任务列表
#         group (List[int]): 每个工人的状态列表
#         n (int): 每个工人最多时间

#     Returns:
#         bool: 是否能够完成
#     """
#     if not jobs:
#         return True

#     v = jobs.pop()
#     for i in range(len(group)):
#         if group[i]+v <= n:
#             group[i] += v
#             if backtrace(jobs, group, n):
#                 return True
#             group[i] -= v

#             if group[i] == 0:
#                 break
#     jobs.append(v)
#     return False


# class Solution:
#     def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

#         def check(limit: int):
#             arr = sorted(jobs)
#             groups = [0]*k
#             return backtrace(arr, groups, limit)

#         lo, hi = 0, sum(jobs)
#         while lo < hi:
#             mid = (lo + hi) // 2
#         if check(mid):
#             hi = mid
#         else:
#             lo = mid+1
#         return lo


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k == len(jobs):
            return max(jobs)

        def dfs(num, groups, target):
            if not num:
                return True
            v = num.pop()
            for i, group in enumerate(groups):
                # print(i,num,v)
                if group + v <= target:
                    groups[i] += v
                    if dfs(num, groups, target):
                        return True
                    groups[i] -= v
                if not group:  # 剪枝按照顺序分配
                    break
            num.append(v)
            return False

        jobs.sort()
        i, j = jobs[-1], sum(jobs)
        while i < j:
            mid = i + (j - i) // 2
            # print(i,j,mid)
            if dfs(jobs[:], [0] * k, mid):
                j = mid
            else:
                i = mid + 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTimeRequired(jobs=[3, 2, 3], k=3))
