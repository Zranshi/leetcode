package main

import (
	rs_type "leetcode/type"
)

type TreeNode = rs_type.TreeNode

func deepestLeavesSum(root *TreeNode) int {
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
			break
		}
		idxLevel = nextLevel
	}
	res := 0
	for _, v := range idxLevel {
		res += v.Val
	}
	return res
}
