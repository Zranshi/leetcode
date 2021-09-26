# -*- coding: UTF-8 -*-
# @Time     : 2021/09/25 07:42
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


if __name__ == "__main__":
    print(Solution().replaceSpace(s="We are happy."))
