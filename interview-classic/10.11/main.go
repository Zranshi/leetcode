package main

import "fmt"

// @Time     : 2022/01/08 18:32
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 面试题 10.11. 峰与谷

func wiggleSort(nums []int) {
	for i := 0; i < len(nums)-1; i++ {
		if (i%2 == 1 && nums[i] < nums[i+1]) || (i%2 == 0 && nums[i] > nums[i+1]) {
			nums[i], nums[i+1] = nums[i+1], nums[i]
		}
	}
}

func main() {
	nums := []int{5, 3, 1, 2, 3}
	wiggleSort(nums)
	fmt.Println(nums)
}
