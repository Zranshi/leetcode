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

    def string(self) -> List[str]:
        if not self:
            return []
        que: List[Optional["TreeNode"]] = [self]
        res = []
        while que:
            res.append(
                " ".join(
                    f"{item.val:4}" if item else f"{'None':4}" for item in que
                )
            )

            new_que: List[Optional["TreeNode"]] = []
            for idx in que:
                if idx:
                    new_que.append(idx.left)
                    new_que.append(idx.right)
                else:
                    new_que.append(None)
                    new_que.append(None)
            if not any(new_que):
                break
            que = new_que
        return res

    def __str__(self) -> str:
        return "\n".join(self.string())

    def __repr__(self) -> str:
        return " ".join(self.string())
