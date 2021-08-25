# -*- coding: UTF-8 -*-
# @Time     : 2021/08/24 07:16
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        c = Counter(nums)
        res = [(-c[key], key) for key in c]
        heapq.heapify(res)
        return [heapq.heappop(res)[1] for _ in range(k)]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[3, 0, 1, 0], k=1))
