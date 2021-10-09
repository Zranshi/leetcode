#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/07 15:43
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode as Node


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == "__main__":
    print(Solution().treeToDoublyList(Node.init_by_list([4, 2, 5, 1, 3])))
