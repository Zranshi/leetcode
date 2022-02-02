package main

import "fmt"

// @Time     : 2022/01/24 19:13
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 032. 有效的变位词

func isAnagram(s string, t string) bool {
	if len(s) != len(t) || s == t {
		return false
	}
	set := make([]int, 26)
	for i := 0; i < len(s); i++ {
		set[s[i]-'a']++
		set[t[i]-'a']--
	}
	for i := 0; i < 26; i++ {
		if set[i] != 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isAnagram("a", "a"))
}
