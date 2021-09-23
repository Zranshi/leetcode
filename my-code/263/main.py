# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 06
# @Author   : Ranshi
# @File     : 263. 丑数.py
class Solution:
    def isUgly(self, n: int) -> bool:
        while n != 1:
            num = n
            if num % 2 == 0:
                num /= 2
            if num % 3 == 0:
                num /= 3
            if num % 5 == 0:
                num /= 5
            if n == num:
                return False
            else:
                n = num
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(n=1))
