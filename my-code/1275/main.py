# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 19
# @Author   : Ranshi
# @File     : 1275. 找出井字棋的获胜者.py
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        def checkwin(S):
            for win in wins:
                flag = True
                for pos in win:
                    if pos not in S:
                        flag = False
                        break
                if flag:
                    return True
            return False

        A, B = set(), set()
        for i, (x, y) in enumerate(moves):
            if i % 2 == 0:
                A.add((x, y))
                if checkwin(A):
                    return "A"
            else:
                B.add((x, y))
                if checkwin(B):
                    return "B"

        return "Draw" if len(moves) == 9 else "Pending"


if __name__ == "__main__":
    s = Solution()
    print(s.tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
