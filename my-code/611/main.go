package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/08/04 08:45
// @Author   : Ranshi
// @File     : main.go
func triangleNumber(nums []int) (res int) {
	sort.Ints(nums)
	for i, v := range nums {
		for j := i + 1; j < len(nums); j++ {
			res += sort.SearchInts(nums[j+1:], v+nums[j])
		}
	}
	return
}

func main() {
	fmt.Println(triangleNumber([]int{2, 2, 3, 4}))
}
