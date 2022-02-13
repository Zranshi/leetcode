# -*- coding: UTF-8 -*-
# @Time     : 2021/08/24 06:33
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        K站中转内最便宜的航班

        Args:
            n (int): 航班的数量
            flights (List[List[int]]): 航班
            src (int): 出发地
            dst (int): 目的地
            k (int): 最大中转数量

        Returns:
            int: 最便宜的机票价格
        """
        f = [float("inf")] * n
        f[src] = 0
        ans = float("inf")
        for t in range(1, k + 2):
            g = [float("inf")] * n
            for j, i, cost in flights:
                g[i] = min(g[i], f[j] + cost)
            f = g
            ans = min(ans, f[dst])

        return -1 if ans == float("inf") else ans


if __name__ == "__main__":
    print(
        Solution().findCheapestPrice(
            n=3,
            flights=[
                [0, 1, 100],
                [1, 2, 100],
                [0, 2, 500],
            ],
            src=0,
            dst=2,
            k=1,
        )
    )
