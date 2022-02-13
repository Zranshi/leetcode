# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 09:15
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + i % 2 * nums[i // 2 + 1]
        return max(nums)


if __name__ == "__main__":
    print(Solution().getMaximumGenerated(n=7))
