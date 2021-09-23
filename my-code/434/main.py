# -*- coding: UTF-8 -*-
# @Time     : 2021/08/20 23:18
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def countSegments(self, s: str) -> int:
        return len([item for item in s.split(" ") if item])


if __name__ == "__main__":
    print(Solution().countSegments(""))
