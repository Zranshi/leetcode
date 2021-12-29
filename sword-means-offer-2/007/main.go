package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/12/14 22:37
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 007. 数组中和为 0 的三个数

func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}
	var res = make([][]int, 0)
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		var target = -nums[i]
		var left, right = i + 1, len(nums) - 1
		for left < right {
			var sum = nums[left] + nums[right]
			if sum == target {
				res = append(res, []int{nums[i], nums[left], nums[right]})
				for left < right {
					left++
					if nums[left-1] != nums[left] {
						break
					}
				}
				for left < right {
					right--
					if nums[right+1] != nums[right] {
						break
					}
				}
			} else if sum < target {
				left++
			} else {
				right--
			}
		}
	}
	return res
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
}
