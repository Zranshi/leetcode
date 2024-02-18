# -*- coding: UTF-8 -*-
# @Time     : 2024/02/02 14:33
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1686. 石子游戏 VI


class Solution:
    def stoneGameVI(self, aliceValues: list[int], bobValues: list[int]) -> int:
        value = [[a + b, a, b] for a, b in zip(aliceValues, bobValues)]
        value.sort(reverse=True)
        alice, bob = 0, 0
        for i in range(len(value)):
            if i % 2 == 0:
                alice += value[i][1]
            else:
                bob += value[i][2]
        if alice == bob:
            return 0
        return 1 if alice > bob else -1


print(Solution().stoneGameVI(aliceValues=[2, 4, 3], bobValues=[1, 6, 7]))
