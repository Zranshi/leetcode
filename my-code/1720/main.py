# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 22
# @Author   : Ranshi
# @File     : 1720. 解码异或后的数组.py
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for item in encoded:
            res.append(item ^ res[-1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.decode(encoded=[1, 2, 3], first=1))
