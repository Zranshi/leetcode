package main

import "fmt"

// @Time     : 2021/08/10 22:57
// @Author   : Ranshi
// @File     : main.go

func maxInts(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func jump(nums []int) int {
	length := len(nums)
	end := 0
	maxPosition := 0
	steps := 0
	for i := 0; i < length-1; i++ {
		maxPosition = maxInts(maxPosition, i+nums[i])
		if i == end {
			end = maxPosition
			steps++
		}
	}
	return steps
}

func main() {
	fmt.Println(jump([]int{2, 3, 1, 1, 4}))
}
