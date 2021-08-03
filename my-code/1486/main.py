# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 21
# @Author   : Ranshi
# @File     : 1486. 数组异或操作.py
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = []
        for i in range(n):
            num.append(start + i * 2)
        ans = 0
        for x in num:
            ans = ans ^ x
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.xorOperation(5, 0))
