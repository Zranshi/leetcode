# -*- coding: UTF-8 -*-
# @Time     : 2021/08/17 08:06
# @Author   : Ranshi
# @File     : main.py


class Solution:

    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2:
            return False
        if s.count('LLL') >= 1:
            return False
        return True


if __name__ == '__main__':
    print(Solution().checkRecord(s="PPALLP"))
