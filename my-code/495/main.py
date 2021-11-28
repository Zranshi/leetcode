#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/10 08:44
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 495. 提莫攻击
class Solution:
    def findPoisonedDuration(self, time_series: list[int], duration: int) -> int:
        return duration + sum(
            [
                min(time_series[i + 1] - time_series[i], duration)
                for i in range(len(time_series) - 1)
            ],
        )


if __name__ == "__main__":
    print(Solution().findPoisonedDuration(time_series=[1, 4], duration=2))
