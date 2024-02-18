package main

import (
	"fmt"
	rstype "leetcode/type"
)

type TreeNode = rstype.TreeNode

func rob(root *TreeNode) int {
	var dfs func(*TreeNode) (int, int)
	dfs = func(tn *TreeNode) (int, int) {
		if tn == nil {
			return 0, 0
		}
		la, lb := dfs(tn.Left)
		ra, rb := dfs(tn.Right)
		return max(la, lb) + max(ra, rb), tn.Val + la + ra
	}
	return max(dfs(root))
}

func main() {
	fmt.Println(rob(rstype.TreeNodeInitBySlice([]int{3, 2, 3, 0, 3, 0, 1})))
}
