# -*- coding: UTF-8 -*-
# @Time     : 2021/08/28 09:14
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(numbers)):
            if numbers[i] in mapping:
                return [mapping[numbers[i]] + 1, i + 1]
            else:
                mapping[target - numbers[i]] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
