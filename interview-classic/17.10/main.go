package main

import "fmt"

// @Time     : 2021/7/9 10:39
// @Author   : Ranshi
// @File     : main.go

func majorityElement(nums []int) int {
	res, mark := 0, 1
	for i := range nums {
		if nums[i] != res {
			mark--
			if mark == 0 {
				res = nums[i]
				mark = 1
			}
		} else {
			mark++
		}
	}
	amount := 0
	for i := range nums {
		if nums[i] == res {
			amount++
		}
	}
	if amount*2 > len(nums) {
		return res
	}
	return -1
}

func main() {
	fmt.Println(majorityElement([]int{3, 2}))
}
