# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 59
# @Author   : Ranshi
# @File     : 110. 平衡二叉树.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if (
                leftHeight == -1
                or rightHeight == -1
                or abs(leftHeight - rightHeight) > 1
            ):
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
