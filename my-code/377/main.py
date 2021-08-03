# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 08
# @Author   : Ranshi
# @File     : 377. 组合总和 Ⅳ.py
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 0
        for i in range(1, target + 1):
            for item in nums:
                if item <= i:
                    if dp[i - item] != 0 or i - item == 0:
                        dp[i] += dp[i - item] if i - item != 0 else 1
                else:
                    break
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4(nums=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                  16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
                            target=10))
