#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/13 09:10
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def verifyPostorder(self, postorder: list[int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True


if __name__ == "__main__":
    print(Solution().verifyPostorder(postorder=[1, 6, 3, 2, 5]))
