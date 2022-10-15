# -*- coding: UTF-8 -*-
# @Time     : 2022/10/13 20:19
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 055. 二叉搜索树迭代器

from type.tree_node import TreeNode


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.lst: list[TreeNode] = []

        def dfs(n: TreeNode):
            if n.left:
                dfs(n.left)
            self.lst.append(n)
            if n.right:
                dfs(n.right)

        dfs(root)
        self.idx = -1

    def next(self) -> int:
        self.idx += 1
        return self.lst[self.idx].val

    def hasNext(self) -> bool:
        return self.idx < len(self.lst)
