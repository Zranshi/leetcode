package main

import (
	"fmt"
	rs_type "leetcode/type"
	"math"
)

// @Time     : 2022/10/08 19:06
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 051. 节点之和最大的路径

type TreeNode = rs_type.TreeNode

func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxPathSum(root *TreeNode) (ans int) {
	ans = math.MinInt
	var dfs func(*TreeNode) int
	dfs = func(tn *TreeNode) int {
		if tn == nil {
			return 0
		}

		left := maxInt(dfs(tn.Left), 0)
		right := maxInt(dfs(tn.Right), 0)

		idx := left + right + tn.Val

		ans = maxInt(ans, idx)

		return tn.Val + maxInt(left, right)
	}
	dfs(root)
	return
}

func main() {
	fmt.Println(maxPathSum(rs_type.TreeNodeInitBySlice([]int{1, 2, 3})))
}
