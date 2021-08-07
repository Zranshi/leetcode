package main

import "fmt"

// @Time     : 2021/08/05 14:53
// @Author   : Ranshi
// @File     : main.go

func singleNumber(nums []int) (res int) {
	for i := range nums {
		res ^= nums[i]
	}
	return
}

func main() {
	fmt.Println(singleNumber([]int{2, 2, 1}))
}
