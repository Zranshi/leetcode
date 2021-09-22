package main

import (
	"bytes"
	"fmt"
	"strings"
)

// @Time     : 2021/09/12 08:18
// @Author   : Ranshi
// @File     : main.go

func licenseKeyFormatting(s string, k int) string {
	linkNum := strings.Count(s, "-")
	chNum := len(s) - linkNum
	linkNum = (len(s) - linkNum) / k
	chs := make([]byte, chNum+linkNum)
	chsIdx := len(chs) - 1
	kIdx := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] != '-' {
			chs[chsIdx] = s[i]
			chsIdx--
			kIdx++
			if kIdx == k {
				kIdx = 0
				chs[chsIdx] = '-'
				chsIdx--
			}
		}
	}
	return strings.TrimPrefix(string(bytes.ToUpper(chs)), "-")
}

func main() {
	fmt.Println(licenseKeyFormatting("2-5g-3-J", 2))
}
