package main

import (
	"fmt"
	"strings"
)

// @Time     : 2021/12/22 13:09
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 686. 重复迭加字符串匹配

func repeatedStringMatch(a string, b string) (ans int) {
	ans = len(b) / len(a)
	if strings.Contains(strings.Repeat(a, ans), b) {
		return ans
	} else if strings.Contains(strings.Repeat(a, ans+1), b) {
		return ans + 1
	} else if strings.Contains(strings.Repeat(a, ans+2), b) {
		return ans + 2
	}
	return -1
}

func main() {
	fmt.Println(repeatedStringMatch("abcd", "abcdabcd"))
}
