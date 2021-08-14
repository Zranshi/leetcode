# coding: utf-8
# @Time     : 2021/08/12 08:31
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(num1 + '*' + num2))


if __name__ == '__main__':
    print(Solution().multiply(num1="2", num2="3"))
