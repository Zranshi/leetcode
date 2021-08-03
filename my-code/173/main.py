# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 173. 二叉搜索树迭代器.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = []
        self.idx = 0
        self.inOrder(root)

    def next(self) -> int:
        self.idx += 1
        return self.queue[self.idx - 1]

    def hasNext(self) -> bool:
        if self.idx < len(self.queue):
            return True
        return False

    def inOrder(self, root: TreeNode):
        if root.left:
            self.inOrder(root.left)
        self.queue.append(root.val)
        if root.right:
            self.inOrder(root.right)
