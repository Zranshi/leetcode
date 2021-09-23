# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 12
# @Author   : Ranshi
# @File     : 697. 数组的度.py
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]

        maxNum = minLen = 0
        for count, left, right in mp.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                if minLen > (span := right - left + 1):
                    minLen = span
        return minLen


if __name__ == "__main__":
    s = Solution()
    print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
