package main

import (
	"fmt"
	rstype "leetcode/type"
	"slices"
)

type TreeNode = rstype.TreeNode

func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root := &TreeNode{Val: preorder[0]}
	if len(preorder) > 1 {
		idx := slices.Index(postorder, preorder[1])
		root.Left = constructFromPrePost(preorder[1:2+idx], postorder[:idx+1])
		root.Right = constructFromPrePost(preorder[2+idx:], postorder[idx+1:len(postorder)-1])
	}
	return root
}

func main() {
	fmt.Println(constructFromPrePost([]int{1, 2, 4, 5, 3, 6, 7}, []int{4, 5, 2, 6, 7, 3, 1}))
}
