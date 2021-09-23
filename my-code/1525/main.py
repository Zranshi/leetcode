# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 21
# @Author   : Ranshi
# @File     : 1525. 字符串的好分割数目.py


class Solution:
    def numSplits(self, s: str) -> int:
        from collections import defaultdict

        left = defaultdict(lambda: 0)
        right = defaultdict(lambda: 0)
        for char in s:
            right[char] += 1
        res = 0
        for char in s:
            left[char] += 1
            right[char] -= 1
            if right[char] == 0:
                right.pop(char)
            if len(left) == len(right):
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numSplits("acbadbaada"))
