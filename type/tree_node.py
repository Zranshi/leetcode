# -*- coding: UTF-8 -*-
# @Time     : 2021/09/04 09:14
# @Author   : Ranshi
# @File     : tree_node.py
# @Doc      : TreeNode 类


from typing import List, Optional
from collections import deque


class TreeNode(object):
    def __init__(
        self,
        val=None,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def init_by_list(cls, lst: list, idx: int = 0) -> Optional["TreeNode"]:
        if idx < len(lst) and lst[idx]:
            return TreeNode(
                val=lst[idx],
                left=TreeNode.init_by_list(lst, idx * 2 + 1),
                right=TreeNode.init_by_list(lst, idx * 2 + 2),
            )

    def __str__(self) -> str:
        level_node: List[List[str]] = [[]]
        dq = deque([(self, 0)])
        while dq:
            idx, idx_level = dq.pop()
            if idx_level >= len(level_node):
                level_node.append([])
            if idx:
                level_node[idx_level].append(f"{idx.val:4}")
                dq.appendleft((idx.left, idx_level + 1))
                dq.appendleft((idx.right, idx_level + 1))
            else:
                level_node[idx_level].append(f"{None:4}")
        return "\n".join(" ".join(item) for item in level_node)
