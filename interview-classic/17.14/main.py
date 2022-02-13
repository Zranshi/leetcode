# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 12:27
# @Author   : Ranshi
# @File     : 123.py


from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        import heapq

        res = []
        heapq.heapify(arr)
        for _ in range(k):
            res.append(heapq.heappop(arr))
        return res


if __name__ == "__main__":
    print(Solution().smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4))
