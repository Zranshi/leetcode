# coding: utf-8
# @Time     : 2021/08/12 16:40
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            idx = ""
            if i % 3 == 0:
                idx += "Fizz"
            if i % 5 == 0:
                idx += "Buzz"
            elif i % 3 != 0:
                idx += str(i)
            res.append(idx)
        return res


if __name__ == "__main__":
    print(Solution().fizzBuzz(50))
