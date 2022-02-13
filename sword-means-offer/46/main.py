# -*- coding: UTF-8 -*-
# @Time     : 2021/10/01 08:31
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def translateNum(self, num: int) -> int:
        def dfs(idx: str) -> int:
            if len(idx) in [0, 1]:
                return 1
            elif int(idx[0]) == 0 or int(idx[0]) > 2 or (int(idx[0]) == 2 and int(idx[1]) > 5):
                return dfs(idx[1:])
            else:
                return dfs(idx[1:]) + dfs(idx[2:])

        return dfs(str(num))


if __name__ == "__main__":
    print(Solution().translateNum(506))
