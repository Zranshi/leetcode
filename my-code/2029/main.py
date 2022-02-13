# -*- coding: UTF-8 -*-
# @Time     : 2022/01/20 09:50
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 2029. 石子游戏 IX
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            if (typ := val % 3) == 0:
                cnt0 += 1
            elif typ == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2


if __name__ == "__main__":
    print(Solution().stoneGameIX(stones=[2, 1]))
