# -*- coding:utf-8 -*-
# @Time     : 2021/6/24 22: 20
# @Author   : Ranshi
# @File     : 1281. 整数的各位积和之差.py


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add, mul = 0, 1
        while n:
            idx = n % 10
            n //= 10
            add += idx
            mul *= idx
        return mul - add


if __name__ == "__main__":
    s = Solution()
    print(s.subtractProductAndSum(n=234))
