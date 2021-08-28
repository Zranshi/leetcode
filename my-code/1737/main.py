# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 22
# @Author   : Ranshi
# @File     : 1737. 满足三条件之一需改变的最少字符数.py
from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        length_a = len(a)
        length_b = len(b)
        a = Counter(a)
        b = Counter(b)
        res = min(
            length_a - a.most_common(1)[0][1], length_b - b.most_common(1)[0][1]
        )
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minCharacters(a="dabadd", b="cda"))
