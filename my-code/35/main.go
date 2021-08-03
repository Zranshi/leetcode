package main

import "fmt"

// @Time     : 2021/7/22 21:26
// @Author   : Ranshi
// @File     : main.go

func searchInsert(nums []int, target int) (res int) {
	lo, hi, res := 0, len(nums)-1, len(nums)
	for lo <= hi {
		mid := (lo + hi) >> 1
		if nums[mid] >= target {
			res = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return
}

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
}
