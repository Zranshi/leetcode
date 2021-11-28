#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/21 07:43
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 559. N 叉树的最大深度
class Node(object):
    def __init__(self, val=None, children=None) -> None:
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        return max(self.maxDepth(item) for item in root.children) + 1 if root.children else 1
