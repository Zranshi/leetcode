# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 57
# @Author   : Ranshi
# @File     : 81. 搜索旋转排序数组 II.py
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for x in nums:
            if target == x:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
