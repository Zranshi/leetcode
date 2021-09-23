# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 13:01
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generate_board():
            board = list()
            for i in range(n):
                r[queens[i]] = "Q"
                board.append("".join(r))
                r[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generate_board()
                res.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        res = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        r = ["."] * n
        backtrack(0)
        return res


if __name__ == "__main__":
    print(Solution().solveNQueens(n=4))
