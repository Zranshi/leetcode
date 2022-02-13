# coding: utf-8
# @Time     : 2021/08/12 16:24
# @Author   : Ranshi
# @File     : 123.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        merged = TreeNode(
            val=root1.val + root2.val,
            left=self.mergeTrees(root1.left, root2.left),
            right=self.mergeTrees(root1.right, root2.right),
        )
        return merged


if __name__ == "__main__":
    ...
