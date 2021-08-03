package main

func checkPossibility(nums []int) bool {
	length, check := len(nums), 0
	for i := 1; i < length; i++ {
		if nums[i] < nums[i-1] {
			check++
			if i+1 < length && i-2 >= 0 {
				if nums[i+1] < nums[i-1] && nums[i-2] > nums[i] {
					return false
				}
			}
		}
		if check > 1 {
			return false
		}
	}
	return true
}
