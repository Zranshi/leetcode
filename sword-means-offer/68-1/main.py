#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/11 08:58
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == "__main__":
    print(
        Solution().lowestCommonAncestor(
            TreeNode.init_by_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            p=2,
            q=8,
        )
    )
