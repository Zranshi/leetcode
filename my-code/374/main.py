# -*- coding:utf-8 -*-
# @Time     : 2021/6/14 08: 54
# @Author   : Ranshi
# @File     : 374. 猜数字大小.py
def guess(i: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if guess(mid) == -1:
                hi = mid - 1
            elif guess(mid) == 1:
                lo = mid + 1
            else:
                return mid
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(n=10))
