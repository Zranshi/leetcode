package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/10/13 19:14
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 054. 所有大于等于节点的值之和

type TreeNode = rs_type.TreeNode

func convertBST(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	lst := []*TreeNode{}
	var dfs func(*TreeNode)
	dfs = func(tn *TreeNode) {
		if tn.Right != nil {
			dfs(tn.Right)
		}
		lst = append(lst, tn)
		if tn.Left != nil {
			dfs(tn.Left)
		}
	}
	dfs(root)
	sum := 0
	for i := 0; i < len(lst); i++ {
		sum += lst[i].Val
		lst[i].Val = sum
	}
	return root
}

func main() {
	fmt.Println(convertBST(rs_type.TreeNodeInitBySlice([]int{3, 2, 4, 1})))
}
