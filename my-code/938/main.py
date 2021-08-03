# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 938. 二叉搜索树的范围和.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val < low:
                return self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                return self.rangeSumBST(root.left, low, high)
            else:
                return root.val + self.rangeSumBST(root.left, low, high) + \
                       self.rangeSumBST(root.right, low, high)
        return 0
