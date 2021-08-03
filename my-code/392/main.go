package main

// @Time     : 2021/5/31 15:35
// @Author   : Ranshi
// @File     : 392. 判断子序列.go
func isSubsequence(s string, t string) bool {
	Idx1, Idx2 := 0, 0
	for Idx1 < len(t) && Idx2 < len(s) {
		if t[Idx1] == s[Idx2] {
			Idx2++
			Idx1++
		} else {
			Idx1++
		}
	}
	return Idx2 == len(s)
}
