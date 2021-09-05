# -*- coding: UTF-8 -*-
# @Time     : 2021/09/05 18:02
# @Author   : Ranshi
# @File     : main.py


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(le: int, ri: int) -> None:
            if le == ri:
                res.append(nums[:])
            else:
                for i in range(le, ri):
                    nums[le], nums[i] = nums[i], nums[le]
                    backtrace(le + 1, ri)
                    nums[le], nums[i] = nums[i], nums[le]

        backtrace(0, len(nums))
        return res


if __name__ == "__main__":
    print(Solution().permute(nums=[1, 2, 3]))
