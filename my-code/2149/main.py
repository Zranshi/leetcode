# -*- coding: UTF-8 -*-
# @Time     : 2022/01/27 13:35
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 2149. 按符号重排数组
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        up_nums, down_nums = [x for x in nums if x > 0], [x for x in nums if x < 0]
        up_ptr, down_ptr = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = up_nums[up_ptr]
                up_ptr += 1
            else:
                nums[i] = down_nums[down_ptr]
                down_ptr += 1
        return nums


if __name__ == "__main__":
    print(Solution().rearrangeArray(nums=[3, 1, -2, -5, 2, -4]))
