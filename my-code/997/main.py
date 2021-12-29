# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 09:49
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = []
        for i in range(n):
            a.append(i + 1)
        for i in range(len(trust)):
            if trust[i][0] in a:
                a.remove(trust[i][0])
        for i in a:
            b = 0
            for j in trust:
                if j[1] == i:
                    b += 1
            if b == n - 1:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().findJudge(n=2, trust=[[1, 2]]))

test = ["Hello", "World", "FishC"]
print(*test, sep="_")
