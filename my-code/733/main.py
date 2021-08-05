# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 09:57
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        from collections import deque
        row, col = len(image), len(image[0])
        dq, path = deque(), {(sr, sc)}
        color = image[sr][sc]
        dq.append((sr, sc))
        while dq:
            idx_r, idx_c = dq.pop()
            image[idx_r][idx_c] = newColor
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_r, next_c = idx_r + r, idx_c + c
                if 0 <= next_r < row and 0 <= next_c < col and image[next_r][
                        next_c] == color and (next_r, next_c) not in path:
                    path.add((next_r, next_c))
                    dq.append((next_r, next_c))
        return image


if __name__ == '__main__':
    print(Solution().floodFill(
        image=[
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
        ],
        sr=1,
        sc=1,
        newColor=2,
    ))
