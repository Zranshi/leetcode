# -*- coding: UTF-8 -*-
# @Time     : 2022/01/07 08:46
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1614. 括号的最大嵌套深度
class Solution:
    def maxDepth(self, s: str) -> int:
        stk_depth = 0
        res = 0
        for ch in s:
            if ch == "(":
                stk_depth += 1
            elif ch == ")":
                stk_depth -= 1
            res = max(res, stk_depth)
        return res


if __name__ == "__main__":
    print(Solution().maxDepth(s="(1+(2*3)+((8)/4))+1"))
