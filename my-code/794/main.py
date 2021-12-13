#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/09 09:55
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 794. 有效的井字游戏
class Solution:
    def win(self, board: list[str], p: str) -> bool:
        return (
            any(
                board[i][0] == p
                and board[i][1] == p
                and board[i][2] == p
                or board[0][i] == p
                and board[1][i] == p
                and board[2][i] == p
                for i in range(3)
            )
            or board[0][0] == p
            and board[1][1] == p
            and board[2][2] == p
            or board[0][2] == p
            and board[1][1] == p
            and board[2][0] == p
        )

    def validTicTacToe(self, board: list[str]) -> bool:
        oCount = sum(row.count("O") for row in board)
        xCount = sum(row.count("X") for row in board)
        return not (
            oCount != xCount
            and oCount != xCount - 1
            or oCount != xCount
            and self.win(board, "O")
            or oCount != xCount - 1
            and self.win(board, "X")
        )


if __name__ == "__main__":
    print(Solution().validTicTacToe(board=["XOX", " X ", "   "]))
