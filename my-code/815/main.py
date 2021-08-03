# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 10: 05
# @Author   : Ranshi
# @File     : 815. 公交路线.py
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import deque
        routes = {i: set(item) for i, item in enumerate(routes)}
        dq, path = deque(), set()
        dq.appendleft((source, 0))
        res = 0
        while dq:
            idx, res = dq[-1]
            if idx == target:
                break
            for i in routes:
                if i not in path and idx in routes[i]:
                    path.add(i)
                    for next_step in routes[i]:
                        if next_step != idx:
                            dq.appendleft((next_step, res + 1))
            dq.pop()
        return res if dq else -1


if __name__ == '__main__':
    s = Solution()
    print(s.numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12))
