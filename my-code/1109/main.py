# -*- coding: UTF-8 -*-
# @Time     : 2021/08/31 08:05
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff, plants = [0 for _ in range(n + 2)], [0 for _ in range(n)]
        for v in bookings:
            diff[v[0]] += v[2]
            diff[v[1] + 1] += -v[2]
        plants[0] = diff[1]
        for i in range(1, n):
            plants[i] = plants[i - 1] + diff[i + 1]
        return plants


if __name__ == "__main__":
    print(
        Solution().corpFlightBookings(
            bookings=[
                [1, 2, 10],
                [2, 3, 20],
                [2, 5, 25],
            ],
            n=5,
        )
    )
