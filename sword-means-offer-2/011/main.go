package main

import "fmt"

// @Time     : 2021/12/15 18:36
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 011. 0 和 1 个数相同的子数组

func findMaxLength(nums []int) (maxLength int) {
	mp := map[int]int{0: -1}
	counter := 0
	for i, num := range nums {
		if num == 1 {
			counter++
		} else {
			counter--
		}
		if prevIndex, has := mp[counter]; has {
			maxLength = max(maxLength, i-prevIndex)
		} else {
			mp[counter] = i
		}
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(findMaxLength([]int{0, 1}))
}
