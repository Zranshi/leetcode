# -*- coding: UTF-8 -*-
# @Time     : 2021/09/05 23:43
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        ...


if __name__ == "__main__":
    print(Solution().searchBST(TreeNode.init_by_list([4, 2, 7, 1, 3, None, None], val=5)))
