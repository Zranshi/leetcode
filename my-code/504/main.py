# -*- coding: UTF-8 -*-
# @Time     : 2022/03/13 14:09
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 504. 七进制数
class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = False
        if num < 0:
            flag = True
            num = -num
        res = []
        while num != 0 or not res:
            num, mod = num.__divmod__(7)
            res.append(mod)
        if flag:
            res.append("-")
        return "".join([str(item) for item in res[::-1]])


print(Solution().convertToBase7(num=-0))
