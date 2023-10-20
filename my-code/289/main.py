# -*- coding: UTF-8 -*-
# @Time     : 2023/10/19 18:15
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 289. 生命游戏


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        # 0 是死, 1是活, 2是原本为死但下一状态活, 3是原本活但下一状态死
        row, col = len(board), len(board[0])

        def next_state(x: int, y: int) -> int:
            live_count = 0
            for i in range(max(0, x - 1), min(row, x + 2)):
                for j in range(max(0, y - 1), min(col, y + 2)):
                    if i == x and j == y:
                        continue
                    live_count += 1 if board[i][j] in [1, 3] else 0
            if live_count in [2, 3]:
                if board[x][y] == 0 and live_count == 3:
                    return 2
                else:
                    return board[x][y]
            return 3 if board[x][y] == 1 else 0

        for i in range(row):
            for j in range(col):
                board[i][j] = next_state(i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        return


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
]
Solution().gameOfLife(board)
for v in board:
    print(v)
