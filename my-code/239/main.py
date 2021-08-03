# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 06
# @Author   : Ranshi
# @File     : 239. 滑动窗口最大值.py
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
