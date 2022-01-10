package main

import "fmt"

// @Time     : 2022/01/10 21:11
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 018. 有效的回文

func isPalindrome(s string) bool {
	byteArr := []byte{}
	for i := 0; i < len(s); i++ {
		b := s[i]
		if b >= 'a' && b <= 'z' {
			byteArr = append(byteArr, b)
		} else if b >= 'A' && b <= 'Z' {
			byteArr = append(byteArr, b+'a'-'A')
		} else if b >= '0' && b <= '9' {
			byteArr = append(byteArr, b)
		}
	}
	left, right := 0, len(byteArr)-1
	for left < right {
		if byteArr[left] != byteArr[right] {
			return false
		}
		left, right = left+1, right-1
	}
	return true
}

func main() {
	fmt.Println(isPalindrome("race a car"))
}
