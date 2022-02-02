package main

import "fmt"

// @Time     : 2022/01/22 15:23
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1332. 删除回文子序列
func removePalindromeSub(s string) int {
	n := len(s)
	for i := 0; i < n; i++ {
		if s[i] != s[n-i-1] {
			return 2
		}
	}
	return 1
}

func main() {
	fmt.Println(removePalindromeSub("ababa"))
}
