package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/09/27 00:24
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 046. 二叉树的右侧视图

type TreeNode = rs_type.TreeNode

func rightSideView(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}
	idxLevel := []*TreeNode{root}

	for len(idxLevel) != 0 {
		ans = append(ans, idxLevel[len(idxLevel)-1].Val)
		nextLevel := []*TreeNode{}
		for _, v := range idxLevel {
			if v.Left != nil {
				nextLevel = append(nextLevel, v.Left)
			}
			if v.Right != nil {
				nextLevel = append(nextLevel, v.Right)
			}
		}
		idxLevel = nextLevel
	}
	return
}

func main() {
	fmt.Println(rightSideView(rs_type.TreeNodeInitBySlice([]int{1, 2, 3, 0, 5, 0, 4})))
}
