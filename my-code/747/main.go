package main

import "fmt"

// @Time     : 2022/01/13 10:17
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 747. 至少是其他数字两倍的最大数

func dominantIndex(nums []int) int {
	maxIdx := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] > nums[maxIdx] {
			maxIdx = i
		}
	}
	for i := 0; i < len(nums); i++ {
		if i != maxIdx && nums[i]*2 > nums[maxIdx] {
			return -1
		}
	}
	return maxIdx
}

func main() {
	fmt.Println(dominantIndex([]int{3, 6, 1, 0}))
}
