# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 566. 重塑矩阵.py
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int,
                      c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape(nums=[[1, 2], [3, 4], [4, 6], [4, 8]], r=2, c=4))
