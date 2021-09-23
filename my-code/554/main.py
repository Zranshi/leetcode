# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 554. 砖墙.py
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        levels = len(wall)
        levelSum = sum(wall[0])
        gap = {0: levels}
        for level in wall:
            index = 0
            for x in level:
                if index + x in gap:
                    gap[index + x] -= 1
                else:
                    gap[index + x] = levels - 1
                index += x
        gap[levelSum] = levels
        return min(gap.values())


if __name__ == "__main__":
    s = Solution()
    print(
        s.leastBricks(
            [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
        )
    )
