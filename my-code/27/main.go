package main

func removeElement(nums []int, val int) (idx int) {
	idx = 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[idx] = nums[i]
			idx++
		}
	}
	return
}
