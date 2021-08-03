# -*- coding:utf-8 -*-
# @Time     : 2021/6/24 23: 56
# @Author   : Ranshi
# @File     : 面试题 01.03. URL化.py
class Solution:
    def replaceSpaces(self, string: str, length: int) -> str:
        return string[:length].replace(' ', '%20')


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpaces("Mr John Smith    ", 13))
