package main

import "fmt"

// @Time     : 2021/6/13 08:49
// @Author   : Ranshi
// @File     : 278. 第一个错误的版本.go
func isBadVersion(version int) bool {
	return true
}

func firstBadVersion(n int) int {
	l, r := 1, n
	for l < r {
		mid := (r + l) / 2
		fmt.Println(mid)
		if isBadVersion(mid) {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	if isBadVersion(l) {
		return l
	} else {
		return l + 1
	}
}
