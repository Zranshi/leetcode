# -*- coding: UTF-8 -*-
# @Time     : 2022/02/11 11:07
# @Author   : Ranshi
# @File     : main.py
# @Doc      :
from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        return [f"{i}/{j}" for i in range(1, n) for j in range(i + 1, n + 1) if gcd(i, j) == 1]


if __name__ == "__main__":
    print(Solution().simplifiedFractions(n=2))
