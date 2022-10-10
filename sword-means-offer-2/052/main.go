package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/10/08 19:21
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 052. 展平二叉搜索树

type TreeNode = rs_type.TreeNode

func increasingBST(root *TreeNode) *TreeNode {
	nodes := []*TreeNode{}
	var dfs func(*TreeNode)
	dfs = func(tn *TreeNode) {
		if tn.Left != nil {
			dfs(tn.Left)
		}
		nodes = append(nodes, tn)
		if tn.Right != nil {
			dfs(tn.Right)
		}
	}
	dfs(root)
	for i := 0; i < len(nodes); i++ {
		nodes[i].Left = nil
		if i != len(nodes)-1 {
			nodes[i].Right = nodes[i+1]
		}
	}
	return nodes[0]
}

func main() {
	// fmt.Println(increasingBST(rs_type.TreeNodeInitBySlice([]int{5, 3, 6, 2, 4, 0, 8, 1, 0, 0, 0, 7, 9})))
	fmt.Println(rs_type.TreeNodeInitBySlice([]int{1, 2, 3, 4, 0, 6, 7, 8, 9, 10}))
}
