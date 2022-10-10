package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/10/08 07:25
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 049. 从根节点到叶节点的路径数字之和

type TreeNode = rs_type.TreeNode

func sumNumbers(root *TreeNode) (ans int) {
	stk := []int{}
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		stk = append(stk, node.Val)
		if node.Left == nil && node.Right == nil {
			idx := 0
			for _, v := range stk {
				idx *= 10
				idx += v
			}
			ans += idx
		} else {
			if node.Left != nil {
				dfs(node.Left)
			}
			if node.Right != nil {
				dfs(node.Right)
			}
		}
		stk = stk[:len(stk)-1]
	}

	dfs(root)
	return
}

func main() {
	fmt.Println(sumNumbers(rs_type.TreeNodeInitBySlice([]int{4, 9, 0, 5, 1})))
}
