package main

import (
	"fmt"
	rs_type "leetcode/type"
	"math"
)

// @Time     : 2022/09/25 19:56
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 044. 二叉树每层的最大值

type TreeNode = rs_type.TreeNode

func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func largestValues(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	ans := []int{}
	idxLevel := []*TreeNode{root}
	for len(idxLevel) != 0 {
		nextLevel := []*TreeNode{}
		max := math.MinInt
		for _, v := range idxLevel {
			if v.Left != nil {
				nextLevel = append(nextLevel, v.Left)
			}
			if v.Right != nil {
				nextLevel = append(nextLevel, v.Right)
			}
			max = maxInt(max, v.Val)
		}
		ans = append(ans, max)
		idxLevel = nextLevel
	}
	return ans
}

func main() {
	fmt.Println(largestValues(rs_type.TreeNodeInitBySlice([]int{1, 3, 2, 5, 3, 0, 9})))
}
