# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 14
# @Author   : Ranshi
# @File     : 779. 第K个语法符号.py
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return 0 if bin(K - 1).count('1') % 2 == 0 else 1


if __name__ == "__main__":
    s = Solution()
    print(s.kthGrammar(4, 5))
