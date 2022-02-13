# -*- coding: UTF-8 -*-
# @Time     : 2021/10/03 07:37
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        # 符号是否相同
        if (
            (numerator > 0 and denominator > 0)
            or (numerator < 0 and denominator < 0)
            or numerator == 0
        ):
            flag = 1
        else:
            flag = -1

        numerator = abs(numerator)
        denominator = abs(denominator)

        # 处理整数部分
        int_part = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return "-" + str(int_part) if flag < 0 else str(int_part)

        # 处理小数部分
        decimal_part = []
        remainder_dict = {}

        while remainder != 0:
            if remainder in remainder_dict:
                pos = remainder_dict[remainder]
                decimal_part.insert(pos, "(")
                decimal_part.append(")")
                break

            remainder_dict[remainder] = len(decimal_part)
            remainder *= 10
            decimal_part.append(str(remainder // denominator))
            remainder = remainder % denominator

        return (
            "-" + str(int_part) + "." + "".join(decimal_part)
            if flag < 0
            else str(int_part) + "." + "".join(decimal_part)
        )


if __name__ == "__main__":
    print(Solution().fractionToDecimal(numerator=1, denominator=2))
