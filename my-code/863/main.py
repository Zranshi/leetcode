from typing import Dict, List, Optional, Set


class TreeNode:
    def __init__(
        self,
        x: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res: List[int] = []
        father_node_map: Dict[TreeNode, Optional[TreeNode]] = {root: None}
        stk: List[TreeNode] = [root]
        path: Set[TreeNode] = {target}
        while stk:
            idx = stk.pop()
            if idx.left:
                father_node_map[idx.left] = idx
                stk.append(idx.left)
            if idx.right:
                father_node_map[idx.right] = idx
                stk.append(idx.right)

        def dfs(idx: TreeNode, distance: int) -> None:
            path.add(idx)
            if distance == k:
                res.append(idx.val)
            else:
                if idx.left and idx.left not in path:
                    dfs(idx.left, distance + 1)
                if idx.right and idx.right not in path:
                    dfs(idx.right, distance + 1)
                father = father_node_map[idx]
                if father and father not in path:
                    dfs(father, distance + 1)

        dfs(target, 0)
        return res
