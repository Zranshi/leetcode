package main

import "fmt"

// @Time     : 2021/12/14 22:35
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 006. 排序数组中两个数字之和

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	idx := 0
	for left < right {
		idx = numbers[left] + numbers[right]
		if idx > target {
			right--
		} else if idx < target {
			left++
		} else {
			return []int{left, right}
		}
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{1, 2, 4, 6, 10}, 8))
}
