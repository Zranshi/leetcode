package main

import "fmt"

// @Time     : 2021/08/06 09:07
// @Author   : Ranshi
// @File     : main.go

func sortColors(nums []int) {
	start, end := 0, len(nums)-1
	for idx := 0; idx <= end; idx++ {
		if nums[idx] == 0 {
			nums[start], nums[idx] = nums[idx], nums[start]
			start++
		} else if nums[idx] == 2 {
			nums[end], nums[idx] = nums[idx], nums[end]
			end--
			if nums[idx] != 1 {
				idx--
			}
		}
	}
}

func main() {
	nums := []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
	fmt.Printf("%v\n", nums)
}
