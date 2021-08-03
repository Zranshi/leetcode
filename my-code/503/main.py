# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 10
# @Author   : Ranshi
# @File     : 503. 下一个更大元素 II.py
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n, ret, stk = len(nums), [-1] * len(nums), list()
        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))
