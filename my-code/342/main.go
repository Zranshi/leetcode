package main

import (
	"strconv"
	"strings"
)

// @Time     : 2021/5/31 10:12
// @Author   : Ranshi
// @File     : 342. 4的幂.go
func isPowerOfFour(n int) bool {
	if n < 1 {
		return false
	}
	s := strconv.FormatInt(int64(n), 4)
	return s[0:1] == "1" && strings.Count(s, "0") == len(s)-1
}
