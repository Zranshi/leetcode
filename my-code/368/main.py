# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 08
# @Author   : Ranshi
# @File     : 368. 最大整除子集.py
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        f, g = [0] * n, [0] * n
        for i in range(n):
            length, prev = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[j] + 1 > length:
                        length = f[j] + 1
                        prev = j
            f[i] = length
            g[i] = prev

        max_len = idx = -1
        for i in range(n):
            if f[i] > max_len:
                idx = i
                max_len = f[i]

        ans = []
        while len(ans) < max_len:
            ans.append(nums[idx])
            idx = g[idx]
        ans.reverse()
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.largestDivisibleSubset(nums=[1, 2, 3, 4, 8]))
