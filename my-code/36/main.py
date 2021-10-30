# -*- coding: UTF-8 -*-
# @Time     : 2021/08/29 16:08
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        L = 9

        def is_repeat_or_add(val, repeat_set: set):
            if val in repeat_set:
                return True
            repeat_set.add(val)
            return False

        for i in range(L):
            repeat_col = set()
            repeat_row = set()

            for j in range(L):
                if board[i][j] != "." and is_repeat_or_add(board[i][j], repeat_row):
                    return False

                if board[j][i] != "." and is_repeat_or_add(board[j][i], repeat_col):
                    return False

        for i, j in ((i, j) for i in range(0, L, 3) for j in range(0, L, 3)):
            repeat = set()
            for next_i, next_j in ((i, j) for i in range(0, 3) for j in range(0, 3)):
                idx = board[i + next_i][j + next_j]
                if idx != "." and is_repeat_or_add(idx, repeat):
                    return False
        return True


if __name__ == "__main__":
    print(
        Solution().isValidSudoku(
            board=[
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
