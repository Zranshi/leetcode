package main

import (
	"fmt"
	rstype "leetcode/type"
	"slices"
)

type TreeNode = rstype.TreeNode

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 && len(inorder) == 0 {
		return nil
	}
	idx := slices.Index(inorder, preorder[0])
	return &TreeNode{
		Val:   preorder[0],
		Left:  buildTree(preorder[1:1+idx], inorder[:idx]),
		Right: buildTree(preorder[1+idx:], inorder[idx+1:]),
	}
}

func main() {
	fmt.Println(buildTree([]int{3, 9, 20, 15, 7}, []int{9, 3, 15, 20, 7}))
}
