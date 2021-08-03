# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 605. 种花问题.py
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        def isEmpty(index: int) -> bool:
            return True if index < 0 or index >= length or \
                           flowerbed[index] == 0 else False

        for i in range(length):
            if n == 0:
                break
            if flowerbed[i] == 0 and isEmpty(i - 1) and isEmpty(i + 1):
                flowerbed[i] = 1
                n -= 1
        return True if n == 0 else False

    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i

        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2

        return count >= n


if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0, 1, 0, 0], n=0))
