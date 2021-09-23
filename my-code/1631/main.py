# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 21
# @Author   : Ranshi
# @File     : 1631. 最小体力消耗路径.py
from collections import deque
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right, ans = 0, 10 ** 6 - 1, 0
        while left <= right:
            mid = (left + right) // 2
            q = deque([(0, 0)])
            seen = {(0, 0)}

            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and (nx, ny) not in seen
                        and abs(heights[x][y] - heights[nx][ny]) <= mid
                    ):
                        q.append((nx, ny))
                        seen.add((nx, ny))
            if (m - 1, n - 1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
