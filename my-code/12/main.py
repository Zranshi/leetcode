# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 49
# @Author   : Ranshi
# @File     : 12. 整数转罗马数字.py
class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def intToRoman(self, num: int) -> str:
        roman = []
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3))
