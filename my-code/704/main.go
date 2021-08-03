package main

import "fmt"

// @Time     : 2021/7/22 21:18
// @Author   : Ranshi
// @File     : main.go

func search(nums []int, target int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mi := (hi+lo)/2
		if nums[mi] > target {
			hi = mi - 1
		} else if nums[mi] < target {
			lo = mi + 1
		} else {
			return mi
		}
	}
	return -1
}

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 12))
}
