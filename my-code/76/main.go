package main

import (
	"fmt"
	"math"
)

// @Time     : 2022/01/26 10:16
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 76. 最小覆盖子串

func minWindow(s string, t string) string {
	ori, cnt := make(map[byte]int, 52), make(map[byte]int, 52)
	for i := 0; i < len(t); i++ {
		ori[t[i]]++
	}
	sLen := len(s)
	len := math.MaxInt32
	ansL, ansR := -1, -1
	check := func() bool {
		for k, v := range ori {
			if cnt[k] < v {
				return false
			}
		}
		return true
	}
	for l, r := 0, 0; r < sLen; r++ {
		if r < sLen && ori[s[r]] > 0 {
			cnt[s[r]]++
		}
		for check() && l <= r {
			if r-l+1 < len {
				len = r - l + 1
				ansL, ansR = l, l+len
			}
			if _, ok := ori[s[l]]; ok {
				cnt[s[l]] -= 1
			}
			l++
		}

	}
	if ansL == -1 {
		return ""
	}
	return s[ansL:ansR]
}

func main() {
	fmt.Println(minWindow("ADOBECODEBANC", "ABC"))
}
