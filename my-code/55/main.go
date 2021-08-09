package main

import "fmt"

// @Time     : 2021/08/08 23:24
// @Author   : Ranshi
// @File     : main.go

func canJump(nums []int) bool {
	maxLength := 0
	for i := 0; i <= maxLength && i < len(nums); i++ {
		if maxLength < i+nums[i] {
			maxLength = i + nums[i]
		}
	}
	return maxLength >= len(nums)-1
}

func main() {
	fmt.Println(canJump([]int{2, 3, 1, 1, 4}))
}
