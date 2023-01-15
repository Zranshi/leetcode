# -*- coding: UTF-8 -*-
# @Time     : 2022/12/05 17:53
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 074. 合并区间
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        n = 1
        res = []
        idx = [intervals[0][0], intervals[0][1]]
        while n < len(intervals):
            node = intervals[n]
            if idx[1] < node[0]:
                res.append(idx)
                idx = [node[0], node[1]]
            else:
                idx = [idx[0], max(idx[1], node[1])]
            n += 1
        res.append(idx)
        return res


if __name__ == "__main__":
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
