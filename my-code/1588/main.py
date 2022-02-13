# -*- coding: UTF-8 -*-
# @Time     : 2021/08/29 08:38
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        pre = [0] + [x for x in arr]
        for i in range(1, len(pre)):
            pre[i] = pre[i - 1] + pre[i]

        for left in range(len(arr)):
            for right in range(left + 1, len(arr) + 1, 2):
                res += pre[right] - pre[left]

        return res


if __name__ == "__main__":
    print(Solution().sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]))
