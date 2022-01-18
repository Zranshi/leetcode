package main

import (
	"fmt"
)

// @Time     : 2022/01/11 17:37
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 020. 回文子字符串的个数
func countSubstrings(s string) int {
	n := len(s)
	ans := 0
	for i := 0; i < 2*n-1; i++ {
		l, r := i/2, i/2+i%2
		for l >= 0 && r < n && s[l] == s[r] {
			l--
			r++
			ans++
		}
	}
	return ans
}

func main() {
	fmt.Println(countSubstrings("aaa"))
}
