# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 21: 19
# @Author   : Ranshi
# @File     : 面试题 01.06. 字符串压缩.py
from typing import List


class Solution:
    def compressString(self, string: str) -> str:
        if not string:
            return string
        res: List[str] = []
        pre, length = string[0], 0
        for ch in string:
            if ch == pre:
                length += 1
            else:
                res.append(str(pre))
                res.append(str(length))
                pre, length = ch, 1
        res.append(str(pre))
        res.append(str(length))
        ans = "".join(res)
        return ans if len(ans) < len(string) else string


if __name__ == "__main__":
    s = Solution()
    print(s.compressString("abbccccccccd"))
