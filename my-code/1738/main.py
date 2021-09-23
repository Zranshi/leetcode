# -*- coding:utf-8 -*-"
# @Time     : 2021/5/19 08:42
# @Author   : Ranshi
# @File     : 1738. 找出第 K 大的异或坐标值.py
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        results = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (
                    pre[i - 1][j]
                    ^ pre[i][j - 1]
                    ^ pre[i - 1][j - 1]
                    ^ matrix[i - 1][j - 1]
                )
                results.append(pre[i][j])
        results.sort(reverse=True)
        return results[k - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.kthLargestValue(matrix=[[5, 2], [1, 6]], k=1))
