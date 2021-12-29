package main

import (
	"fmt"
)

// @Time     : 2021/12/15 13:20
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 010. 和为 k 的子数组

func subarraySum(nums []int, k int) (ans int) {
	n := len(nums)
	pre := make([]int, n+1)
	for i := 0; i < n; i++ {
		pre[i+1] = pre[i] + nums[i]
	}
	for right := 1; right < n+1; right++ {
		for left := 0; left < right; left++ {
			if pre[right]-pre[left] == k {
				ans++
			}
		}
	}
	return
}

func main() {
	fmt.Println(subarraySum([]int{1, 1, 1}, 2))
}
