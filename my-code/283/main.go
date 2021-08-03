package main

// @Time     : 2021/5/30 21:55
// @Author   : Ranshi
// @File     : 283. 移动零.go

// 冒泡思想
func _moveZeroes(nums []int) {
	for right := len(nums) - 1; right >= 0; right-- {
		for idx := 0; idx < right; idx++ {
			if nums[idx] == 0 && nums[idx+1] != 0 {
				nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
			}
		}
		if nums[right] != 0 {
			break
		}
	}
}

// 双指针
func moveZeroes(nums []int) {
	zeros, length := 0, len(nums)
	for idx := 0; idx < length; idx++ {
		if nums[idx] == 0 {
			zeros++
		} else {
			nums[idx-zeros] = nums[idx]
		}
	}
	for i := length - 1; i >= length-zeros; i-- {
		nums[i] = 0
	}
}
