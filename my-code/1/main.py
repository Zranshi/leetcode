# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 13: 17
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s: dict[int, int] = {}  # 将已经读取的元素放入哈希表中, 其中目标值为key, 列表下标为val.
        for i in range(len(nums)):
            if nums[i] in s:
                return [s[nums[i]], i]
            else:
                s[target - nums[i]] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
