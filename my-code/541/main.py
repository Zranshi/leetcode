# -*- coding: UTF-8 -*-
# @Time     : 2021/08/20 08:22
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        i = 0

        def rev_str(le, ri):
            while le < ri:
                res[le], res[ri] = res[ri], res[le]
                le, ri = le + 1, ri - 1

        for i in range(2 * k, len(s), 2 * k):
            rev_str(i - 2 * k, i - k - 1)
        else:
            rev_str(i, (len(s) - 1 if len(s) - i <= k else i + k - 1))

        return "".join(res)


if __name__ == "__main__":
    print(Solution().reverseStr(s="abcdefg", k=2))
