# -*- coding: UTF-8 -*-
# @Time     : 2024/01/28 01:01
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 365. 水壶问题


class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        stack: list[tuple[int, int]] = [(0, 0)]
        seen = set()
        flag = False
        while stack:
            x, y = stack.pop()
            if x == targetCapacity or y == targetCapacity or x + y == targetCapacity:
                flag = True
                break
            if (x, y) in seen:
                continue
            seen.add((x, y))

            stack.append((jug1Capacity, y))

            stack.append((x, jug2Capacity))

            stack.append((0, y))

            stack.append((x, 0))

            pour = min(x, jug2Capacity - y)
            stack.append((x - pour, y + pour))

            pour = min(y, jug1Capacity - x)
            stack.append((x + pour, y - pour))
        return flag


print(Solution().canMeasureWater(jug1Capacity=3, jug2Capacity=5, targetCapacity=4))
