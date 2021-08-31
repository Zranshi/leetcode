# -*- coding: UTF-8 -*-
# @Time     : 2021/08/31 08:39
# @Author   : Ranshi
# @File     : main.py


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(26):
            ch = chr(ord('a') + i)
            if magazine.count(ch) < ransomNote.count(ch):
                return False
        return True


if __name__ == '__main__':
    print(Solution().canConstruct(ransomNote="a", magazine="b"))
