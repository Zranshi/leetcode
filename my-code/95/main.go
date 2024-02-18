package main

import (
	"fmt"
	rstype "leetcode/type"
)

type TreeNode = rstype.TreeNode

func generateTrees(n int) []*TreeNode {
	var fun func(start, end int) []*TreeNode
	fun = func(start, end int) []*TreeNode {
		if start > end {
			return []*TreeNode{nil}
		}
		allTrees := []*TreeNode{}
		for i := start; i <= end; i++ {
			leftTrees := fun(start, i-1)
			rightTrees := fun(i+1, end)
			for _, left := range leftTrees {
				for _, right := range rightTrees {
					currTree := &TreeNode{Val: i, Left: left, Right: right}
					allTrees = append(allTrees, currTree)
				}
			}
		}
		return allTrees
	}
	return fun(1, n)
}

func main() {
	fmt.Println(generateTrees(3))
}
