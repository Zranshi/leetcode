package main

import (
	"fmt"
	rstype "leetcode/type"
)

type TreeNode = rstype.TreeNode

func inorderTraversal(root *TreeNode) []int {
    res := []int{}
	if root == nil {
		return res
	}
	res = append(res, inorderTraversal(root.Left)...)
    res = append(res, root.Val)
	res = append(res, inorderTraversal(root.Right)...)
	return res
}

func main() {
	fmt.Println(inorderTraversal(rstype.TreeNodeInitBySlice([]int{1, 0, 2, 3})))
}
