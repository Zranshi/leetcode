package main

import "fmt"

// @Time     : 2021/08/09 18:48
// @Author   : Ranshi
// @File     : main.go

func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))
	res[0] = 1
	for i := 1; i < len(nums); i++ {
		res[i] = nums[i-1] * res[i-1]
	}
	R := 1
	for i := len(nums) - 1; i >= 0; i-- {
		res[i] = res[i] * R
		R *= nums[i]
	}
	return res
}

func main() {
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
}
