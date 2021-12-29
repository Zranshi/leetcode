package main

import "fmt"

// @Time     : 2021/12/16 23:15
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 012. 左右两边子数组的和相等

func pivotIndex(nums []int) int {
	ans := -1
	if len(nums) <= 1 {
		return ans
	}
	pre := make([]int, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		pre[i+1] = pre[i] + nums[i]
	}
	for i := 1; i < len(pre); i++ {
		left := pre[i-1]
		right := pre[len(pre)-1] - pre[i]
		if left == right {
			return i - 1
		}
	}
	return -1
}

func main() {
	fmt.Println(pivotIndex([]int{-1, -1, 0, 1, 1, 0}))
}
