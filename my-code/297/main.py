# -*- coding: UTF-8 -*-
# @Time     : 2021/08/22 07:52
# @Author   : Ranshi
# @File     : main.py

from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    from collections import deque

    def serialize(self, root):
        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("None")
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        if not data:
            return []
        dataList = data[1:-1].split(",")
        root = TreeNode(int(dataList[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if dataList[i] != "None":
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if dataList[i] != "None":
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root
