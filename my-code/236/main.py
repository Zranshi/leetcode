# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 06
# @Author   : Ranshi
# @File     : 236. 二叉树的最近公共祖先.py
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self,
            root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in (None, p, q):
            return root
        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)
        return R if L else L if R else root
