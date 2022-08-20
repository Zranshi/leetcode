package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/08/20 09:25
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 654. 最大二叉树

type TreeNode = rs_type.TreeNode

func constructMaximumBinaryTree(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	max := 0
	for i, v := range nums {
		if nums[max] < v {
			max = i
		}
	}
	return &TreeNode{
		Val:   nums[max],
		Left:  constructMaximumBinaryTree(nums[:max]),
		Right: constructMaximumBinaryTree(nums[max+1:]),
	}
}

func main() {
	fmt.Println(constructMaximumBinaryTree([]int{3, 2, 1, 6, 0, 5}))
}
