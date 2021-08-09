package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/08/08 15:26
// @Author   : Ranshi
// @File     : main.go
func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func deleteAndEarn(nums []int) int {
	sort.Ints(nums)
	arr := []int{nums[0]}
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			arr[len(arr)-1] += nums[i]
		} else {
			if nums[i] > nums[i-1]+1 {
				arr = append(arr, 0)
			}
			arr = append(arr, nums[i])
		}
	}
	if len(arr) == 1 {
		return arr[0]
	}
	dp := make([]int, len(arr))
	dp[0] = arr[0]
	dp[1] = maxInt(arr[0], arr[1])
	for i := 2; i < len(arr); i++ {
		dp[i] = maxInt(dp[i-1], arr[i]+dp[i-2])
	}
	return dp[len(dp)-1]
}

func main() {
	fmt.Println(deleteAndEarn([]int{2, 3}))
}
