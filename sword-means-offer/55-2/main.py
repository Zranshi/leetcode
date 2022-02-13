#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/09 12:46
# @Author   : Ranshi
# @File     : 123.py
from type.tree_node import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


if __name__ == "__main__":
    print(Solution().isBalanced(TreeNode.init_by_list([3, 9, 20, None, None, 15, 7])))
