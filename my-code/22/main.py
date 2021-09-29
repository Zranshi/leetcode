# -*- coding:utf-8 -*-
# @Time     : 2021/6/13 22: 20
# @Author   : Ranshi
# @File     : 22. 括号生成.py
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(a):
            if len(a) == 2 * n:
                if valid(a):
                    ans.append("".join(a))
            else:
                _extracted_from_generate_6(a, "(")
                _extracted_from_generate_6(a, ")")

        # TODO Rename this here and in `generate`
        def _extracted_from_generate_6(a, arg1):
            a.append(arg1)
            generate(a)
            a.pop()

        def valid(a):
            bal = 0
            for c in a:
                if c == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(n=3))
