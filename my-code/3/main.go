package main

import "fmt"

// @Time     : 2021/08/03 23:29
// @Author   : Ranshi
// @File     : main.go

func lengthOfLongestSubstring(s string) (res int) {
	mapping := map[byte]bool{}
	left := 0
	for right := 0; right < len(s); right++ {
		if mapping[s[right]] {
			for s[left] != s[right] {
				mapping[s[left]] = false
				left++
			}
			left++
		} else {
			mapping[s[right]] = true
		}
		if res < right-left+1 {
			res = right - left + 1
		}
	}
	return
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
}
