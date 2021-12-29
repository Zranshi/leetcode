package main

import (
	"fmt"
	"math"
	"sort"
)

// @Time     : 2021/12/14 23:06
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 008. 和大于等于 target 的最短子数组

func minSubArrayLen(s int, nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	ans := math.MaxInt32
	sums := make([]int, n+1)
	for i := 1; i <= n; i++ {
		sums[i] = sums[i-1] + nums[i-1]
	}
	for i := 1; i <= n; i++ {
		target := s + sums[i-1]
		bound := sort.SearchInts(sums, target)
		if bound < 0 {
			bound = -bound - 1
		}
		if bound <= n {
			ans = min(ans, bound-(i-1))
		}
	}
	if ans == math.MaxInt32 {
		return 0
	}
	return ans
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	fmt.Println(minSubArrayLen(7, []int{2, 3, 1, 2, 4, 3}))
}
