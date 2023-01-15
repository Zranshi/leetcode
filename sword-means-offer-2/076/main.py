# -*- coding: UTF-8 -*-
# @Time     : 2022/12/05 18:30
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 076. 数组中的第 k 大的数字
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq

        nums = [-item for item in nums]
        heapq.heapify(nums)
        while k > 1:
            k -= 1
            heapq.heappop(nums)
        return -heapq.heappop(nums)


if __name__ == "__main__":
    print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
