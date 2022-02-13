# -*- coding: UTF-8 -*-
# @Time     : 2021/09/21 20:36
# @Author   : Ranshi
# @File     : 123.py
from typing import Callable, List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]


def bisect(n: int, f: Callable[[int], bool]) -> int:
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if f(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]))
