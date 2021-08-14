package main

import "fmt"

// @Time     : 2021/08/10 09:10
// @Author   : Ranshi
// @File     : main.go

func numberOfArithmeticSlices(nums []int) (ans int) {
	if len(nums) == 1 {
		return
	}
	d, t := nums[0]-nums[1], 0
	for i := 2; i < len(nums); i++ {
		if nums[i-1]-nums[i] == d {
			t++
		} else {
			d, t = nums[i-1]-nums[i], 0
		}
		ans += t
	}
	return
}

func main() {
	fmt.Println(numberOfArithmeticSlices([]int{1, 2, 3, 4}))
}
