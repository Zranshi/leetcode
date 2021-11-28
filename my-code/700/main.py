#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/26 14:44
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 700. 二叉搜索树中的搜索
from pyal.container import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        return None


if __name__ == "__main__":
    print(Solution().searchBST(TreeNode.init_by_lst([4, 2, 7, 1, 3, None, None]), val=5))
