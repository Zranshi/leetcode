package main

import "fmt"

func maxSubArray(nums []int) int {
	_max := nums[0]
	for _, v := range nums {
		_max = max(_max, v)
	}
	if _max <= 0 {
		return _max
	}
	res := 0
	for _, v := range nums {
		res += v
		if res < 0 {
			res = 0
		} else if res > _max {
			_max = res
		}
	}
	return _max
}

func main() {
	fmt.Println(maxSubArray([]int{-2, -1, -3, -4, -1, -2, -1, -5, -4}))
}
