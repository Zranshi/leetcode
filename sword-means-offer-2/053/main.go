package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/10/10 23:04
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 053. 二叉搜索树中的中序后继

type TreeNode = rs_type.TreeNode

func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	lst := []*TreeNode{}
	var dfs func(*TreeNode)
	dfs = func(tn *TreeNode) {
		if tn.Left != nil {
			dfs(tn.Left)
		}
		lst = append(lst, tn)
		if tn.Right != nil {
			dfs(tn.Right)
		}
	}
	dfs(root)
	for i := 0; i < len(lst)-1; i++ {
		if lst[i].Val == p.Val {
			return lst[i+1]
		}
	}
	return nil
}

func main() {
	fmt.Println(inorderSuccessor(nil, nil))
}
