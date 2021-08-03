# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 24
# @Author   : Ranshi
# @File     : 1834. 单线程 CPU.py
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])

        ans = list()
        q = list()
        timestamp = 0
        ptr = 0

        for i in range(n):
            if not q:
                timestamp = max(timestamp, tasks[indices[ptr]][0])
            while ptr < n and tasks[indices[ptr]][0] <= timestamp:
                heapq.heappush(q, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1
            process, index = heapq.heappop(q)
            timestamp += process
            ans.append(index)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getOrder(
        tasks=[[46, 9], [46, 42], [30, 46], [30, 13], [30, 24], [30, 5],
               [30, 21], [29, 46], [29, 41], [29, 18],
               [29, 16], [29, 17], [29, 5], [22, 15], [22, 13], [22, 25],
               [22, 49], [22, 44]]))
