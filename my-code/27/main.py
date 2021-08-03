# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 50
# @Author   : Ranshi
# @File     : 27. 移除元素.py
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for x in nums:
            if x != val:
                nums[idx] = x
                idx += 1
        return idx


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
