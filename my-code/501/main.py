# -*- coding:utf-8 -*-
# @Time     : 2021/7/4 21: 37
# @Author   : Ranshi
# @File     : main.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        counter = {}

        def pre_order(idx: TreeNode):
            if idx:
                if idx.val in counter:
                    counter[idx.val] += 1
                else:
                    counter[idx.val] = 1
                pre_order(idx.left)
                pre_order(idx.right)

        pre_order(root)
        res = []
        _max = 0
        for key in counter:
            _max = max(_max, counter[key])
        for key in counter:
            if counter[key] == _max:
                res.append(key)
        return res
