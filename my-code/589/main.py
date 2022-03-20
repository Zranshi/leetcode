# -*- coding: UTF-8 -*-
# @Time     : 2022/03/16 21:52
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 589. N 叉树的前序遍历
class Node:
    def __init__(self, val=None, children=None) -> None:
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> list[int]:
        if not root:
            return []
        res = []
        stk = [root]
        while stk:
            idx = stk.pop()
            res.append(idx.val)
            stk.extend(idx.children[::-1])
        return res
