package main

import "fmt"

// @Time     : 2021/5/28 23:43
// @Author   : Ranshi
// @File     : 167. 两数之和 II - 输入有序数组.go

func twoSum(ints []int, target int) []int {
	left, right := 0, len(ints)-1
	for left < right {
		val := ints[left] + ints[right]
		if val == target {
			return []int{left + 1, right + 1}
		} else if val > target {
			right--
		} else {
			left++
		}
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 3, 4}, 6))
}
