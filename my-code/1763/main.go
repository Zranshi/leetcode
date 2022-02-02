package main

import (
	"fmt"
	"math/bits"
	"unicode"
)

// @Time     : 2022/02/01 10:14
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1763. 最长的美好子字符串

func longestNiceSubstring(s string) (ans string) {
	mask := uint(0)
	for _, ch := range s {
		mask |= 1 << (unicode.ToLower(ch) - 'a')
	}
	maxTypeNum := bits.OnesCount(mask)

	for typeNum := 1; typeNum <= maxTypeNum; typeNum++ {
		var lowerCnt, upperCnt [26]int
		var total, cnt, l int
		for r, ch := range s {
			idx := unicode.ToLower(ch) - 'a'
			if unicode.IsLower(ch) {
				lowerCnt[idx]++
				if lowerCnt[idx] == 1 && upperCnt[idx] > 0 {
					cnt++
				}
			} else {
				upperCnt[idx]++
				if upperCnt[idx] == 1 && lowerCnt[idx] > 0 {
					cnt++
				}
			}
			if lowerCnt[idx]+upperCnt[idx] == 1 {
				total++
			}

			for total > typeNum {
				idx := unicode.ToLower(rune(s[l])) - 'a'
				if lowerCnt[idx]+upperCnt[idx] == 1 {
					total--
				}
				if unicode.IsLower(rune(s[l])) {
					lowerCnt[idx]--
					if lowerCnt[idx] == 0 && upperCnt[idx] > 0 {
						cnt--
					}
				} else {
					upperCnt[idx]--
					if upperCnt[idx] == 0 && lowerCnt[idx] > 0 {
						cnt--
					}
				}
				l++
			}

			if cnt == typeNum && r-l+1 > len(ans) {
				ans = s[l : r+1]
			}
		}
	}
	return
}

func main() {
	fmt.Println(longestNiceSubstring("YazaAay"))
}
