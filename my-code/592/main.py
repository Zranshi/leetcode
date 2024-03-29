# -*- coding: UTF-8 -*-
# @Time     : 2022/07/27 12:06
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 592. 分数加减运算
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        denominator, numerator = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            denominator1, sign = 0, 1
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1
            denominator1 = sign * denominator1
            i += 1

            # 读取分母
            numerator1 = 0
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1

            denominator = denominator * numerator1 + denominator1 * numerator
            numerator *= numerator1
        if denominator == 0:
            return "0/1"
        g = gcd(abs(denominator), numerator)
        return f"{denominator // g}/{numerator // g}"


if __name__ == "__main__":
    print(Solution().fractionAddition("-1/2+1/2"))
