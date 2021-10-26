#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/24 07:55
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 638. 大礼包
from functools import lru_cache


class Solution:
    def shoppingOffers(
        self, price: list[int], special: list[list[int]], needs: list[int]
    ) -> int:
        """
        自顶向下记忆化搜索.

        Args:
            price (list[int]): 价格数组
            special (list[list[int]]): 礼包数组
            needs (list[int]): 需求数组

        Returns:
            int: 最小花费
        """
        n = len(price)
        filter_special = [
            sp
            for sp in special
            if sum(sp[i] for i in range(n)) > 0
            and sum(sp[i] * price[i] for i in range(n)) > sp[-1]
        ]

        @lru_cache(None)
        def dfs(cur_needs):
            min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
            for cur_special in filter_special:
                special_price = cur_special[-1]
                next_needs = []
                for i in range(n):
                    if cur_special[i] > cur_needs[i]:
                        break
                    next_needs.append(cur_needs[i] - cur_special[i])
                if len(next_needs) == n:
                    min_price = min(
                        min_price, dfs(tuple(next_needs)) + special_price
                    )
            return min_price

        return dfs(tuple(needs))


if __name__ == "__main__":
    print(
        Solution().shoppingOffers(
            price=[2, 5], special=[[3, 0, 5], [1, 2, 10]], needs=[3, 2]
        )
    )
