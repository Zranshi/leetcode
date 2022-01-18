# -*- coding: UTF-8 -*-
# @Time     : 2022/01/15 08:42
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1716. 计算力扣银行的钱
class Solution:
    def totalMoney(self, n: int) -> int:
        week_num, days = divmod(n, 7)
        return (
            (1 + days) * days // 2
            + week_num * days
            + (28 + (28 + 7 * (week_num - 1))) * week_num // 2
        )


if __name__ == "__main__":
    print(Solution().totalMoney(n=10))
