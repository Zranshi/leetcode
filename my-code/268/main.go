package main

// @Time     : 2021/5/30 21:35
// @Author   : Ranshi
// @File     : 268. 丢失的数字.go
func missingNumber(nums []int) int {
	max := len(nums)
	sum := max * (max + 1) / 2
	for _, item := range nums {
		sum -= item
	}
	return sum
}
