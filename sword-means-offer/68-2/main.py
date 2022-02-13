#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/11 09:20
# @Author   : Ranshi
# @File     : 123.py
from type.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root in (p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == "__main__":
    print(
        Solution().lowestCommonAncestor(
            TreeNode.init_by_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            p=5,
            q=1,
        )
    )
