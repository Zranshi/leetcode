package main

import "fmt"

// @Time     : 2021/08/03 19:49
// @Author   : Ranshi
// @File     : main.go

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		another := target - nums[i]
		if _, ok := m[another]; ok {
			return []int{m[another], i}
		}
		m[nums[i]] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{1, 2, 34, 5, 52, 3, 1, 4, 5, 6, 7}, 8))
}
