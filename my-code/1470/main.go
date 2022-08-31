package main

import "fmt"

// @Time     : 2022/08/29 13:55
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1470. 重新排列数组

func shuffle(nums []int, n int) []int {
	ans := make([]int, len(nums))
	for i := range ans {
		if i%2 == 0 {
			ans[i] = nums[i/2]
		} else {
			ans[i] = nums[i/2+n]
		}
	}
	return ans
}

func main() {
	fmt.Println(shuffle([]int{1, 2, 3, 4, 4, 3, 2, 1}, 4))
}
