package main

// @Time     : 2021/5/31 11:02
// @Author   : Ranshi
// @File     : 349. 两个数组的交集.go
func intersection(nums1 []int, nums2 []int) []int {
	m := make(map[int]struct{})
	ans := make([]int, 0)
	for _, v := range nums1 {
		m[v] = struct{}{}
	}
	for _, v := range nums2 {
		if _, ok := m[v]; ok {
			delete(m, v)
			ans = append(ans, v)
		}
	}
	return ans
}
