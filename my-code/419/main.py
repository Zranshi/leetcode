#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/18 08:54
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 419. 甲板上的战舰


class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        ans = 0
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == "X":
                    row[j] = "."
                    for k in range(j + 1, n):
                        if row[k] != "X":
                            break
                        row[k] = "."
                    for k in range(i + 1, m):
                        if board[k][j] != "X":
                            break
                        board[k][j] = "."
                    ans += 1
        return ans


if __name__ == "__main__":
    print(
        Solution().countBattleships(
            board=[
                ["X", ".", ".", "X"],
                [".", ".", ".", "X"],
                [".", ".", ".", "X"],
            ]
        )
    )
