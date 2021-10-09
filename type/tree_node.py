# -*- coding: UTF-8 -*-
# @Time     : 2021/09/04 09:14
# @Author   : Ranshi
# @File     : tree_node.py
# @Doc      : TreeNode 类
from typing import List, Optional


class TreeNode(object):
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" = None,
        right: "TreeNode" = None,
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
        return None

    def __string(self) -> List[str]:
        level = [self]
        res = []
        while any(item is not None for item in level):
            res.append(
                " ".join(f"{item.val:<4}" if item else "None" for item in level)
            )
            next_level = [None] * len(level) * 2
            for i, item in enumerate(level):
                next_level[i * 2] = item.left if item and item.left else None
                next_level[i * 2 + 1] = (
                    item.right if item and item.right else None
                )
            level = next_level
        return res

    def __str__(self) -> str:
        return "\n".join(self.__string())

    def __repr__(self) -> str:
        return " ".join(self.__string())
