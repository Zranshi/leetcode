# -*- coding: UTF-8 -*-
# @Time     : 2022/01/28 21:37
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1996. 游戏中弱角色的数量
class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        maxDef = 0
        for _, def_ in properties:
            if maxDef > def_:
                ans += 1
            else:
                maxDef = max(maxDef, def_)
        return ans


if __name__ == "__main__":
    print(
        Solution().numberOfWeakCharacters(
            properties=[[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]
        )
    )
