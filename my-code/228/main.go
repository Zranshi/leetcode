package main

import (
	"strconv"
)

func summaryRanges(nums []int) (ans []string) {
	left, right, length := 0, 0, len(nums)
	for right < length {
		if right != length-1 && nums[right]+1 == nums[right+1] {
			right++
		} else {
			if nums[left] == nums[right] {
				ans = append(ans, strconv.Itoa(nums[left]))
			} else {
				ans = append(ans, strconv.Itoa(nums[left])+"->"+strconv.Itoa(nums[right]))
			}
			left, right = right+1, right+1
		}
	}
	return ans
}
