# -*- coding:utf-8 -*-
# @Time     : 2021/7/4 21: 52
# @Author   : Ranshi
# @File     : main.py
from typing import List

d = {
    '2': 'abd',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        length = len(digits)
        target = []
        res = []

        def dfs(idx: int):
            if idx == length:
                res.append(''.join(target))
            else:
                item = digits[idx]
                for letter in d[item]:
                    target.append(letter)
                    dfs(idx + 1)
                    target.pop()

        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations(digits="23"))
