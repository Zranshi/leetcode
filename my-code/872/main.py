# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 16
# @Author   : Ranshi
# @File     : 872. 叶子相似的树.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        from typing import List

        def inOrder(root: TreeNode, order_list: List[int]):
            if root.left or root.right:
                if root.left:
                    inOrder(root.left, order_list)
                if root.right:
                    inOrder(root.right, order_list)
            else:
                order_list.append(root.val)

        list1, list2 = [], []

        inOrder(root1, list1)
        inOrder(root2, list2)
        return list1 == list2
