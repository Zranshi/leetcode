package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/08/05 14:59
// @Author   : Ranshi
// @File     : main.go

func threeSum(nums []int) (res [][]int) {
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; i++ {
		if nums[i] > 0 {
			break
		} else if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		j, k := i+1, len(nums)-1
		for j < k {
			if nums[j]+nums[k]+nums[i] == 0 {
				res = append(res, []int{nums[i], nums[j], nums[k]})
				j++
				k--
				for j < k && nums[j] == nums[j-1] {
					j++
				}
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			} else if nums[j]+nums[k]+nums[i] < 0 {
				j++
			} else {
				k--
			}
		}
	}
	return res
}

func main() {
	fmt.Println(threeSum([]int{-2, 0, 0, 2, 2}))
}
