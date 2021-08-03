package main

import "fmt"

// @Time     : 2021/07/27 20:25
// @Author   : Ranshi
// @File     : main.go

func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func rob(nums []int) int {
	if len(nums) < 2 {
		return nums[0]
	}
	dp := make([]int, len(nums))
	dp[0], dp[1] = nums[0], maxInt(nums[0], nums[1])
	for i := 2; i < len(nums); i++ {
		dp[i] = maxInt(dp[i-1], nums[i]+dp[i-2])
	}
	return dp[len(dp)-1]
}

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1}))
}
