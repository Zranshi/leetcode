# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 23: 07
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        ret, path = [], []

        def dfs(idx: TreeNode, target: int):
            if not idx:
                return
            path.append(idx.val)
            target -= idx.val
            if not idx.left and not idx.right and target == 0:
                ret.append(path[:])
            dfs(idx.left, target)
            dfs(idx.right, target)
            path.pop()

        dfs(root, target_sum)
        return ret
