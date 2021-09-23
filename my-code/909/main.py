# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 09: 59
# @Author   : Ranshi
# @File     : 909. 蛇梯棋.py
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n, idx_path = len(board), 0
        send, path, dq = {}, {}, deque()
        for i in range(n * n):
            row = n - (i // n) - 1
            col = i % n if i // n % 2 == 0 else n - (i % n) - 1
            if board[row][col] != -1:
                send[i + 1] = board[row][col]
        dq.appendleft((1, 0))
        while dq:
            idx, idx_path = dq[-1]
            if idx == n * n:
                break
            if idx not in path or path[idx] > idx_path:
                path[idx] = idx_path
                for i in range(1, 7):
                    if 1 <= idx + i <= n * n:
                        next_idx = (
                            idx + i if idx + i not in send else send[idx + i]
                        )
                        dq.appendleft((next_idx, idx_path + 1))
            dq.pop()
        return idx_path if dq else -1


if __name__ == "__main__":
    s = Solution()
    print(
        s.snakesAndLadders(
            [
                [-1, -1, 19, 10, -1],
                [2, -1, -1, 6, -1],
                [-1, 17, -1, 19, -1],
                [25, -1, 20, -1, -1],
                [-1, -1, -1, -1, 15],
            ]
        )
    )
