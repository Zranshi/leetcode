package main

import "fmt"

// @Time     : 2021/08/08 14:49
// @Author   : Ranshi
// @File     : main.go
func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func rob(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	} else if len(nums) == 2 {
		return maxInt(nums[0], nums[1])
	} else if len(nums) == 3 {
		return maxInt(maxInt(nums[0], nums[1]), nums[2])
	}
	maxMoney := func(arr []int) int {
		if len(arr) == 1 {
			return arr[0]
		}
		dp := make([]int, len(arr))
		dp[0] = arr[0]
		dp[1] = maxInt(arr[0], arr[1])
		for i := 2; i < len(arr); i++ {
			dp[i] = maxInt(dp[i-1], dp[i-2]+arr[i])
		}
		return dp[len(dp)-1]
	}
	return maxInt(maxMoney(nums[1:]), maxMoney(nums[2:len(nums)-1])+nums[0])
}

func main() {
	fmt.Println(rob([]int{0}))
}
