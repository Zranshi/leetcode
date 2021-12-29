# -*- coding: UTF-8 -*-
# @Time     : 2021/12/21 18:47
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 475. 供暖器
from bisect import bisect_right


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float("inf")
            leftDistance = house - heaters[i] if i >= 0 else float("inf")
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans


if __name__ == "__main__":
    print(Solution().findRadius(houses=[1, 2, 3], heaters=[2]))
