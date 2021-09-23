# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 14: 31
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        from collections import deque

        dq, path = deque(), set()
        old_color, row, col = image[sr][sc], len(image), len(image[0])
        dq.append((sr, sc))
        while dq:
            idx = dq.pop()
            image[idx[0]][idx[1]] = new_color
            path.add(idx)
            for move in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                _next = (idx[0] + move[0], idx[1] + move[1])
                if (
                    0 <= _next[0] < row
                    and 0 <= _next[1] < col
                    and image[_next[0]][_next[1]] == old_color
                    and _next not in path
                ):
                    dq.appendleft(_next)
        return image


if __name__ == "__main__":
    print(
        Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, new_color=2)
    )
