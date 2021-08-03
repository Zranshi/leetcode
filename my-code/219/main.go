package main

// @Time     : 2021/5/30 09:47
// @Author   : Ranshi
// @File     : 219. 存在重复元素 II.go
func containsNearbyDuplicate(nums []int, k int) bool {
	numMap := make(map[int]bool)
	for left, right := 0, 0; right < len(nums); right++ {
		if right-left > k {
			numMap[nums[left]] = false
			left++
		}
		if numMap[nums[right]] {
			return true
		} else {
			numMap[nums[right]] = true
		}
	}
	return false
}
