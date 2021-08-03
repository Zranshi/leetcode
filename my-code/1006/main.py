# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 1006. 笨阶乘.py
class Solution:
    def clumsy(self, n: int) -> int:
        idx = 0
        stack = [n]
        for i in range(n - 1, 0, -1):
            if idx % 4 == 0:
                stack[-1] *= i
            elif idx % 4 == 1:
                stack[-1] = int(stack[-1] / i)
            elif idx % 4 == 2:
                stack.append(i)
            else:
                stack.append(-1 * i)
            idx += 1
        return sum(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(10))
