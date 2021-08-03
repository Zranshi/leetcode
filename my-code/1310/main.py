# -*- coding:utf-8 -*-
# @Time     : 2021/5/12 07:58
# @Author   : Ranshi
# @File     : 1310. 子数组异或查询.py
from typing import List


class Solution:
    def xorQueries(
            self, arr: List[int],
            queries: List[List[int]]) -> List[int]:
        res = []
        pre = [0]
        for x in arr:
            pre.append(pre[-1] ^ x)
        for left, right in queries:
            res.append(pre[right + 1] ^ pre[left])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.xorQueries(arr=[1, 3, 4, 8], queries=[
        [0, 0], [1, 2], [0, 3], [3, 3]]))
