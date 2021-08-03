package main

// @Time     : 2021/6/3 22:05
// @Author   : Ranshi
// @File     : 404. 左叶子之和.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) (ans int) {
	if root.Left != nil {
		if root.Left.Left == nil && root.Left.Right == nil {
			ans += root.Left.Val
		} else {
			ans += sumOfLeftLeaves(root.Left)
		}
	}
	if root.Right != nil {
		ans += sumOfLeftLeaves(root.Right)
	}
	return
}
