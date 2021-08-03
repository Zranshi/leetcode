package main

import "fmt"

// @Time     : 2021/7/22 21:09
// @Author   : Ranshi
// @File     : main.go

func maxSubArray(nums []int) int {
	idx, res := -1, nums[0]
	for i := range nums {
		if idx < 0 {
			idx = nums[i]
		} else {
			idx += nums[i]
		}
		if res < idx {
			res = idx
		}
	}
	return res
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
