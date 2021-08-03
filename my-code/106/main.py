# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 59
# @Author   : Ranshi
# @File     : 106. 从中序与后序遍历序列构造二叉树.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(iOrder, pOrder):
            if not pOrder:
                return None
            root = TreeNode(pOrder[-1])
            rootInx = iOrder.index(root.val)

            root.left = helper(iOrder[0:rootInx], pOrder[0:rootInx])
            root.right = helper(iOrder[rootInx + 1:], pOrder[rootInx:-1])
            return root

        return helper(inorder, postorder)


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
