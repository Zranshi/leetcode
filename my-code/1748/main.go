package main

import "fmt"

// @Time     : 2022/2/6 11:53
// @Author   : rs
// @File     : main.go

func sumOfUnique(nums []int) (ans int) {
	numSet := make(map[int]int, len(nums))
	for i := 0; i < len(nums); i++ {
		numSet[nums[i]]++
	}
	for key, val := range numSet {
		if val == 1 {
			ans += key
		}
	}
	return ans
}

func main() {
	fmt.Println(sumOfUnique([]int{1, 2, 3, 2}))
}
