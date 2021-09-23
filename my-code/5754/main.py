# -*- coding:utf-8 -*-
# @Time     : 2021/5/29 22:30
# @Author   : Ranshi
# @File     : 5754. 长度为三且各字符不同的子字符串.py
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        from collections import Counter

        length = len(s)
        res = 0
        for right in range(3, length + 1):
            flag = True
            c = Counter(s[right - 3 : right])
            for item in c.values():
                if item != 1:
                    flag = False
                    break
            if flag:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countGoodSubstrings(s="xyzzaz"))
