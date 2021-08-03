package main

// @Time     : 2021/5/28 23:43
// @Author   : Ranshi
// @File     : 167. 两数之和 II - 输入有序数组.go

func twoSum2(ints []int, target int) []int {
	left, right := 0, len(ints)-1
	for left != right {
		if ints[left]+ints[right] == target {
			return []int{left + 1, right + 1}
		} else if ints[left]+ints[right] < target {
			left++
		} else {
			right--
		}
	}
	return nil
}
