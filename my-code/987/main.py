# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 19:44
# @Author   : Ranshi
# @File     : main.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, row=0, col=0):
            if node is None:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        ans, nodes = [], []
        dfs(root)
        nodes.sort()

        cur_col = None
        for col, _, val in nodes:
            if col != cur_col:
                cur_col = col
                ans.append([])
            ans[-1].append(val)

        return ans
