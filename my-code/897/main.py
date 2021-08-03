# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 16
# @Author   : Ranshi
# @File     : 897. 递增顺序搜索树.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def InOrder(root: TreeNode):
            if root:
                InOrder(root.left)
                nums.append(root.val)
                InOrder(root.right)

        InOrder(root)

        root.left, root.val, cur = None, nums[0], root

        for i in range(1, len(nums)):
            cur.right = TreeNode(val=nums[i])
            cur = cur.right

        return root
