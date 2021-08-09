package main

import "fmt"

// @Time     : 2021/08/09 18:57
// @Author   : Ranshi
// @File     : main.go

func subarraySum(nums []int, k int) int {
	count, pre := 0, 0
	m := make(map[int]int, len(nums)+1)
	m[0] = 1
	for i := 0; i < len(nums); i++ {
		pre += nums[i]
		if _, ok := m[pre-k]; ok {
			count += m[pre-k]
		}
		m[pre] += 1
	}
	return count
}

func main() {
	fmt.Println(subarraySum([]int{1, 1, 1}, 2))
}
