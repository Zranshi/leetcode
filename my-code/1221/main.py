# -*- coding: UTF-8 -*-
# @Time     : 2021/09/09 17:21
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        l_num, r_num = 0, 0
        for ch in s:
            if ch == "L":
                l_num += 1
            elif ch == "R":
                r_num += 1
            if l_num >= 1 and r_num >= 1 and l_num == r_num:
                res += 1
        return res


if __name__ == "__main__":
    print(Solution().balancedStringSplit(s="RLRRLLRLRL"))
