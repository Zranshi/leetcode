# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 04
# @Author   : Ranshi
# @File     : 228. 汇总区间.py
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res, left, right, length = [], 0, 0, len(nums)
        while right < length:
            if right != length - 1 and nums[right] + 1 == nums[right + 1]:
                right += 1
            else:
                if nums[left] == nums[right]:
                    res.append(f"{nums[right]}")
                else:
                    res.append(f"{nums[left]}->{nums[right]}")
                left, right = right + 1, right + 1
            # print(f"left: {left}, right: {right}, res:{res}")
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
