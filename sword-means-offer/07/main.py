#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/13 08:01
# @Author   : Ranshi
# @File     : main.py
from typing import List
from pyal.container import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(pl, pr, il, ir):
            if pl > pr:
                return None
            proot = preorder[pl]
            iroot = d[proot]
            lsize = iroot - il

            root = TreeNode(proot)
            root.left = dfs(pl + 1, pl + lsize, il, iroot - 1)
            root.right = dfs(pl + lsize + 1, pr, iroot + 1, ir)
            return root

        n = len(preorder)
        d = {j: i for i, j in enumerate(inorder)}
        return dfs(0, n - 1, 0, n - 1)


if __name__ == "__main__":
    print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
