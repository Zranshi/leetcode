package main

import "fmt"

// @Time     : 2021/12/15 12:46
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 009. 乘积小于 K 的子数组

func numSubarrayProductLessThanK(nums []int, k int) (res int) {
	if k == 0 {
		return 0
	}
	left, mul := 0, 1
	n := len(nums)
	for right := 0; right < n; right++ {
		mul *= nums[right]
		for mul >= k && left < right {
			mul /= nums[left]
			left++
		}
		if mul < k {
			res += right - left + 1
		}
	}
	return
}

func main() {
	fmt.Println(numSubarrayProductLessThanK([]int{1, 1, 1}, 1))
}
