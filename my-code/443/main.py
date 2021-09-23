# -*- coding: UTF-8 -*-
# @Time     : 2021/08/21 07:37
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        def reverse(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        n = len(chars)
        write = left = 0
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                num = read - left + 1
                if num > 1:
                    anchor = write
                    while num > 0:
                        chars[write] = str(num % 10)
                        write += 1
                        num //= 10
                    reverse(anchor, write - 1)
                left = read + 1
        return write


if __name__ == "__main__":
    print(Solution().compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
