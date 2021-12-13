#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/03 11:13
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1005. K 次取反后最大化的数组和
from collections import Counter


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break

        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break

        return ans


if __name__ == "__main__":
    print(Solution().largestSumAfterKNegations(nums=[4, 2, 3], k=1))
