#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 11:36
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 37. 序列化二叉树
import collections

from pyal.container import TreeNode


class Codec:
    def serialize(self, root):
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        if data == "[]":
            return
        vals, i = data[1:-1].split(","), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
