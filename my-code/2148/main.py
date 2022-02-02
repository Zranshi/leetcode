# -*- coding: UTF-8 -*-
# @Time     : 2022/01/27 12:19
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 2148. 元素计数
class Solution:
    def countElements(self, nums: list[int]) -> int:
        max_num, min_num = nums[0], nums[0]
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
            if nums[i] < min_num:
                min_num = nums[i]
        return len([x for x in nums if x not in (max_num, min_num)])


if __name__ == "__main__":
    print(Solution().countElements(nums=[11, 7, 2, 15]))
