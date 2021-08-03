package main

// @Time     : 2021/7/16 09:38
// @Author   : Ranshi
// @File     : main.go

import (
	"fmt"
	"sort"
)

func search(nums []int, target int) (res int) {
	for idx := sort.SearchInts(nums, target); idx < len(nums); idx++ {
		if nums[idx] == target {
			res++
		} else {
			break
		}
	}
	return
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(search(nums, 8))
}
