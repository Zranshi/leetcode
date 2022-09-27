package main

import (
	rs_type "leetcode/type"
)

// @Time     : 2022/09/27 00:35
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 047. 二叉树剪枝

type TreeNode = rs_type.TreeNode

func pruneTree(root *TreeNode) *TreeNode {
	var dfs func(*TreeNode) bool
	dfs = func(tn *TreeNode) bool {
		if tn == nil {
			return false
		}
		left, right := dfs(tn.Left), dfs(tn.Right)
		if !left {
			tn.Left = nil
		}
		if !right {
			tn.Right = nil
		}
		return tn.Val == 1 || left || right
	}
	if !dfs(root) {
		return nil
	}
	return root
}
