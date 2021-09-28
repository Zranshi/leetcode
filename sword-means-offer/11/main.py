# -*- coding: UTF-8 -*-
# @Time     : 2021/09/26 22:47
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = (low + high) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]


if __name__ == "__main__":
    print(Solution().minArray([3, 4, 5, 1, 2]))
