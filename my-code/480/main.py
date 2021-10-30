# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 480. 滑动窗口中位数.py
import bisect
from typing import List


class Solution:
    def _medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        left, length = 0, len(nums)
        while left + k <= length:
            _list = sorted(nums[left : left + k])
            res.append(
                _list[len(_list) // 2]
                if len(_list) % 2
                else (_list[len(_list) // 2 - 1] + _list[len(_list) // 2]) / 2
            )
            left += 1
        return res

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(a):
            return a[len(a) // 2] if len(a) % 2 else (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2

        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.pop(bisect.bisect_left(a, i))
            a.insert(bisect.bisect_left(a, j), j)
            res.append(median(a))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
