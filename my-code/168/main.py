# -*- coding:utf-8 -*-
# @Time     : 2021/5/28 23:54
# @Author   : Ranshi
# @File     : 168. Excel表列名称.py
class Solution:

    def convertToTitle(self, num: int) -> str:
        res = []
        while num:
            num -= 1
            res.append(chr(ord('A') + num % 26))
            num //= 26
        return ''.join(res[::-1])


if __name__ == '__main__':
    print(Solution().convertToTitle(700))
