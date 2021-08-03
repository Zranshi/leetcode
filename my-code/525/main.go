package main

// @Time     : 2021/6/3 08:46
// @Author   : Ranshi
// @File     : 525. 连续数组.go

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func findMaxLength(nums []int) (ans int) {
	mp := map[int]int{0: -1}
	counter := 0
	for i, num := range nums {
		if num == 1 {
			counter++
		} else {
			counter--
		}
		if preIndex, has := mp[counter]; has {
			ans = MaxInt(ans, i-preIndex)
		} else {
			mp[counter] = i
		}
	}
	return
}
