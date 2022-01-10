package main

import "fmt"

// @Time     : 2022/01/10 21:18
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 019. 最多删除一个字符得到回文

func validPalindrome(s string) bool {
	var check func(int, int, int) bool
	check = func(l, r, k int) bool {
		for l < r {
			if s[l] != s[r] {
				if k != 0 {
					return check(l+1, r, k-1) || check(l, r-1, k-1)
				} else {
					return false
				}
			}
			l, r = l+1, r-1
		}
		return true
	}
	return check(0, len(s)-1, 1)
}

func main() {
	fmt.Println(validPalindrome("abca"))
}
