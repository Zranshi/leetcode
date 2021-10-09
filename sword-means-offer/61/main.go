package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/10/08 08:52
// @Author   : Ranshi
// @File     : main.go

func isStraight(nums []int) bool {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	zereNum := 0
	distance := 0
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == 0 {
			zereNum++
		} else if nums[i] == nums[i+1] {
			return false
		} else {
			distance += nums[i+1] - nums[i] - 1
		}
	}

	return distance == 0 || zereNum >= distance
}

func main() {
	fmt.Println(isStraight([]int{1, 2, 3, 4, 5}))
}
