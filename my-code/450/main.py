# -*- coding: UTF-8 -*-
# @Time     : 2021/08/20 08:40
# @Author   : Ranshi
# @File     : main.py

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif not root.left and not root.right:
            root = None
        elif root.right:
            root.val = self.successor(root)
            root.right = self.deleteNode(root.right, root.val)
        else:
            root.val = self.predecessor(root)
            root.left = self.deleteNode(root.left, root.val)

        return root


if __name__ == "__main__":
    ...
