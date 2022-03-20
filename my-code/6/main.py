# -*- coding:utf-8 -*-
# @Time     : 2021/05/18 18: 56
# @Author   : Ranshi
# @File     : 6. Z 字形变换.py
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        path = [[] for _ in range(num_rows)]
        idx, mode = 0, 1
        for item in s:
            path[idx].append(item)
            if mode == 1 and idx == num_rows - 1:
                mode = 2
            elif mode == 2 and idx == 0:
                mode = 1
            if mode == 1:
                idx += 1
            else:
                idx -= 1
        return "".join("".join(item) for item in path)


if __name__ == "__main__":
    print(Solution().convert(s="PAYPALISHIRING", num_rows=3))
