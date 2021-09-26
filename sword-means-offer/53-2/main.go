package main

import "fmt"

// @Time     : 2021/09/26 07:27
// @Author   : Ranshi
// @File     : main.go

func missingNumber(nums []int) int {
	ran := len(nums)
	l, r := 0, ran-1
	for l <= r {
		mid := (r-l)/2 + l
		if nums[mid] == mid {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return l
}

func main() {
	fmt.Printf("%v\n", missingNumber([]int{0}))
}
