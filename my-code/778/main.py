# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 14
# @Author   : Ranshi
# @File     : 778. 水位上升的泳池中游泳.py
from collections import deque
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = deque([(0, 0)])
        ans = [[float('inf')] * n for _ in range(n)]
        ans[0][0] = grid[0][0]
        while que:
            x, y = que.popleft()
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                pox = x + i
                poy = y + j
                if 0 <= pox < n and 0 <= poy < n:
                    d = max(grid[pox][poy], int(ans[x][y]))
                    if d < ans[pox][poy]:
                        ans[pox][poy] = d
                        que.append((pox, poy))
        return int(ans[-1][-1])


if __name__ == '__main__':
    s = Solution()
    print(s.swimInWater(
        [[0, 1, 2, 3, 4],
         [24, 23, 22, 21, 5],
         [12, 13, 14, 15, 16],
         [11, 17, 18, 19, 20],
         [10, 9, 8, 7, 6]]))
