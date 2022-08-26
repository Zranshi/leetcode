package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/08/26 01:57
// @Author   : Ranshi
// @File     : mian.go
// @Doc      : 1464. 数组中两元素的最大乘积

func maxProduct(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	return (nums[n-1] - 1) * (nums[n-2] - 1)
}

func main() {
	fmt.Println(maxProduct([]int{1, 5, 4, 5}))
}
