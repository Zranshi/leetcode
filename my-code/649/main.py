# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 649. Dota2 Senate.py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        import collections
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"


if __name__ == "__main__":
    s = Solution()
    print(s.predictPartyVictory("RD"))
