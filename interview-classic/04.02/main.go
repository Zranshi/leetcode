package main

import "fmt"

// @Time     : 2021/6/29 20:06
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) (node *TreeNode) {
	if len(nums) != 0 {
		mid := (0 + len(nums) - 1) / 2
		return &TreeNode{
			Val:   nums[mid],
			Left:  sortedArrayToBST(nums[:mid]),
			Right: sortedArrayToBST(nums[mid+1:]),
		}
	}
	return nil
}

func main() {
	fmt.Println(sortedArrayToBST([]int{-10, -3, 0, 5, 9}))
}
