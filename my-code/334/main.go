package main

import (
	"fmt"
	"math"
)

// @Time     : 2021/08/09 18:20
// @Author   : Ranshi
// @File     : main.go

func increasingTriplet(nums []int) bool {
	if len(nums) < 3 {
		return false
	}
	small, mid := math.MaxInt64, math.MaxInt64
	for _, v := range nums {
		if v <= small {
			small = v
		} else if v <= mid {
			mid = v
		} else {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(increasingTriplet([]int{2, 4, -2, -3}))
}
