# -*- coding:utf-8 -*-
# @Time     : 2021/6/24 12: 43
# @Author   : Ranshi
# @File     : 149. 直线上最多的点数.py
import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 对于每个点，找到同一直线中最多的点数
        res = 1
        n = len(points)
        for i in range(n):
            # 用于记录从当前点，可以构成直线的斜率值，每个斜率k对应的是点数-1
            seen = collections.defaultdict(int)
            for j in range(n):
                # 同一个点：跳过
                if points[i] == points[j]:
                    continue
                # 平行于y轴的直线
                if points[j][0] == points[i][0]:
                    k = float("inf")
                else:
                    # 计算斜率
                    k = (points[j][1] - points[i][1]) / (
                        points[j][0] - points[i][0]
                    )
                seen[k] += 1
            for k in seen.values():
                res = max(res, k + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
