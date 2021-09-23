# -*- coding: UTF-8 -*-
# @Time     : 2021/08/22 07:36
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        LENGTH = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            length = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if length <= LENGTH:
                return False
        return True


if __name__ == "__main__":
    print(
        Solution().escapeGhosts(
            ghosts=[[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]],
            target=[7, 7],
        )
    )
