package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/09/26 23:46
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 045. 二叉树最底层最左边的值

type TreeNode = rs_type.TreeNode

func findBottomLeftValue(root *TreeNode) int {
	idxLevel := []*TreeNode{root}

	for {
		nextLevel := []*TreeNode{}
		for _, v := range idxLevel {
			if v.Left != nil {
				nextLevel = append(nextLevel, v.Left)
			}
			if v.Right != nil {
				nextLevel = append(nextLevel, v.Right)
			}
		}
		if len(nextLevel) == 0 {
			return idxLevel[0].Val
		}
		idxLevel = nextLevel
	}
}

func main() {
	fmt.Println(findBottomLeftValue(rs_type.TreeNodeInitBySlice([]int{1, 2, 3, 4, 0, 5, 6, 0, 0, 7})))
}
