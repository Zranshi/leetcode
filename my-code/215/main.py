# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 02
# @Author   : Ranshi
# @File     : 215. 数组中的第K个最大元素.py
from typing import List


class Solution:
    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        return nums.sort(reverse=True)[k - 1]

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        快速排序,打乱顺序后时间更快
        O(n) O(1)
        """
        import random
        random.shuffle(nums)

        def partition(nums, left, right):
            pivot = nums[left]
            j = left
            for i in range(left + 1, right + 1):
                if nums[i] < pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
                print(nums)

            nums[left], nums[j] = nums[j], nums[left]
            return j

        size = len(nums)
        target = size - k
        left = 0
        right = size - 1
        while True:
            index = partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
