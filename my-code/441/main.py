# -*- coding: UTF-8 -*-
# @Time     : 2021/08/20 23:34
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def arrangeCoins(self, n: int) -> int:
        le, ri = 1, n
        while le < ri:
            mid = (le + ri) // 2
            if n < ((1 + mid) * mid) // 2:
                ri = mid - 1
            elif n < ((2 + mid) * (mid + 1)) // 2:
                return mid
            else:
                le = mid + 1
        return le


if __name__ == "__main__":
    print(Solution().arrangeCoins(n=5))
