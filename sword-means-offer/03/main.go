package main

import "fmt"

// @Time     : 2021/09/25 23:15
// @Author   : Ranshi
// @File     : main.go

func findRepeatNumber(nums []int) int {
	set := make(map[int]bool, len(nums))
	for _, x := range nums {
		if value := set[x]; !value {
			set[x] = true
		} else {
			return x
		}
	}
	return -1
}

func main() {
	fmt.Printf("%v\n", findRepeatNumber([]int{2, 3, 1, 0, 2, 5, 3}))
}
