#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/29 12:10
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 786. 第 K 个最小的素数分数
class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            # 记录最大的分数
            x, y = 0, 1

            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += i + 1

            if count == k:
                return [x, y]

            if count < k:
                left = mid
            else:
                right = mid


if __name__ == "__main__":
    print(Solution().kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
