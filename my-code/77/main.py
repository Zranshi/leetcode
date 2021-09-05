# -*- coding: UTF-8 -*-
# @Time     : 2021/09/05 17:27
# @Author   : Ranshi
# @File     : main.py


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrace(idx: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return
            if idx == n + 1:
                return

            backtrace(idx + 1)

            path.append(idx)
            backtrace(idx + 1)
            path.pop()

        backtrace(1)
        return res


if __name__ == "__main__":
    print(Solution().combine(n=4, k=2))
