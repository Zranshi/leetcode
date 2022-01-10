package main

import "fmt"

// @Time     : 2021/08/03 19:49
// @Author   : Ranshi
// @File     : main.go

func twoSum(nums []int, target int) []int {
	numSet := make(map[int]int, len(nums))
	for i, v := range nums {
		if idx, ok := numSet[target-v]; ok {
			return []int{idx, i}
		}
		numSet[v] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{1, 2, 34, 5, 52, 3, 1, 4, 5, 6, 7}, 8))
}
