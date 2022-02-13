# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 23: 25
# @Author   : Ranshi
# @File     : 123.py
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if not firstNode and pre.val > p.val:
                firstNode = pre
            if firstNode and pre.val > p.val:
                secondNode = p
            pre = p
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
