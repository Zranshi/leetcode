# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 978. 最长湍流子数组.py
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        lo, hi, length, res = 0, 0, len(arr), 1
        while hi < length - 1:
            if lo == hi:
                if arr[lo] == arr[lo + 1]:
                    lo += 1
                hi += 1
            else:
                if arr[hi - 1] < arr[hi] and arr[hi] > arr[hi + 1]:
                    hi += 1
                elif arr[hi - 1] > arr[hi] and arr[hi] < arr[hi + 1]:
                    hi += 1
                else:
                    lo = hi
            res = max(res, hi - lo + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
