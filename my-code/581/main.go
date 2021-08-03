package main

import (
	"fmt"
	"math"
)

// @Time     : 2021/8/3 09:22
// @Author   : Ranshi
// @File     : main.go
// @Doc      :

func findUnsortedSubarray(nums []int) int {
	n := len(nums)
	minn, maxn := math.MaxInt64, math.MinInt64
	left, right := -1, -1
	for i, num := range nums {
		if maxn > num {
			right = i
		} else {
			maxn = num
		}
		if minn < nums[n-i-1] {
			left = n - 1 - i
		} else {
			minn = nums[n-i-1]
		}
	}
	if right == -1 {
		return 0
	}
	return right - left + 1
}

func main() {
	fmt.Println(findUnsortedSubarray([]int{2, 6, 4, 8, 10, 9, 15}))
}
