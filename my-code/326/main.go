package main

import (
	"strconv"
	"strings"
)

// @Time     : 2021/5/30 22:43
// @Author   : Ranshi
// @File     : 326. 3的幂.go
func isPowerOfThree(n int) bool {
	if n < 1 {
		return false
	}
	s := strconv.FormatInt(int64(n), 3)
	return s[0:1] == "1" && strings.Count(s, "0") == len(s)-1
}
