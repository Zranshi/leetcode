# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 14: 01
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def permutation(self, chs: str):
        begin, end = 0, len(chs)
        n = list(chs)
        res = []

        def dfs(arr, le: int, ri: int):
            if le >= ri:
                res.append("".join(arr))
            else:
                i = le
                for num in range(le, ri):
                    arr[num], arr[i] = arr[i], arr[num]
                    dfs(arr, le + 1, ri)
                    arr[num], arr[i] = arr[i], arr[num]

        dfs(n, begin, end)
        return list(set(res))


if __name__ == "__main__":
    print(Solution().permutation("qqe"))
