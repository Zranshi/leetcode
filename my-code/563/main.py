#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/18 11:08
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 563. 二叉树的坡度
from pyal.container import TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)
        return sum_left + sum_right + node.val


if __name__ == "__main__":
    print(Solution().findTilt(TreeNode.init_by_lst([4, 2, 9, 3, 5, None, 7])))
