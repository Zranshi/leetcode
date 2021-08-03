package main

// @Time     : 2021/5/31 10:14
// @Author   : Ranshi
// @File     : 344. 反转字符串.go

func reverseString(s []byte) {
	idx := 0
	reIdx := len(s) - 1
	for idx < reIdx {
		s[idx], s[reIdx] = s[reIdx], s[idx]
		idx++
		reIdx--
	}
}
