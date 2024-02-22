# -*- coding: UTF-8 -*-
# @Time     : 2021/08/19 08:19
# @Author   : Ranshi
# @File     : 123.py

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        idx = inorder.index(preorder[0])
        # 由于Python的切片机制是浅复制, 而不是创建新的列表索引. 所以会创建新的内存空间, 造成空间开销大.
        return TreeNode(
            val=preorder[0],
            left=self.buildTree(preorder[1 : idx + 1], inorder[:idx]),
            right=self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :]),
        )


if __name__ == "__main__":
    print(
        Solution().buildTree(
            preorder=[3, 9, 20, 15, 7],
            inorder=[9, 3, 15, 20, 7],
        )
    )
