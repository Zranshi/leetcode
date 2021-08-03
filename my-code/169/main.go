package main

// @Time     : 2021/5/29 21:38
// @Author   : Ranshi
// @File     : 169. 多数元素.go
func majorityElement(nums []int) int {
	major := 0
	count := 0
	for _, num := range nums {
		if count == 0 {
			major = num
		}
		if major == num {
			count += 1
		} else {
			count -= 1
		}
	}
	return major
}
