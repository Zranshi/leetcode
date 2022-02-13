#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/11 08:55
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def sumNums(self, n: int) -> int:
        return n and self.sumNums(n - 1) + n


if __name__ == "__main__":
    print(Solution().sumNums(n=3))
