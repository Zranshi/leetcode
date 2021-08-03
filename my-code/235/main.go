package main

// @Time     : 2021/5/30 20:39
// @Author   : Ranshi
// @File     : 235. 二叉搜索树的最近公共祖先.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if (root.Val-q.Val)*(root.Val-p.Val) <= 0 {
		return root
	} else if root.Val > q.Val {
		return lowestCommonAncestor(root.Left, p, q)
	} else {
		return lowestCommonAncestor(root.Right, p, q)
	}
}
