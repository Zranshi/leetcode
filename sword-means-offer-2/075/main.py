# -*- coding: UTF-8 -*-
# @Time     : 2022/12/05 18:07
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 075. 数组相对排序
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr2_d = {v: i for i, v in enumerate(arr2)}
        tmp1, tmp2 = [item for item in arr1 if item in arr2_d], [
            item for item in arr1 if item not in arr2_d
        ]
        tmp1.sort(key=lambda x: arr2_d[x])
        tmp2.sort()
        return [*tmp1, *tmp2]


if __name__ == "__main__":
    print(
        Solution().relativeSortArray(
            arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
        )
    )
