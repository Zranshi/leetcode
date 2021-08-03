package main

import "fmt"

// @Time     : 2021/7/22 21:05
// @Author   : Ranshi
// @File     : main.go

func containsDuplicate(nums []int) bool {
	m := make(map[int]bool, len(nums))
	for i := range nums {
		if _, ok := m[nums[i]]; ok {
			if m[nums[i]] {
				return true
			}
		} else {
			m[nums[i]] = true
		}
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}
