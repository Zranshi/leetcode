package main

import (
	"strings"
)

// @Time     : 2021/5/30 22:27
// @Author   : Ranshi
// @File     : 290. 单词规律.go
func wordPattern(pattern string, s string) bool {
	mapping1 := make(map[uint8]string)
	mapping2 := make(map[string]uint8)
	strList := strings.Split(s, " ")
	if len(strList) != len(pattern) {
		return false
	}
	for i, str := range strList {
		if _, ok := mapping1[pattern[i]]; ok {
			if str != mapping1[pattern[i]] {
				return false
			}
		} else {
			mapping1[pattern[i]] = str
		}
		if _, ok := mapping2[str]; ok {
			if pattern[i] != mapping2[str] {
				return false
			}
		} else {
			mapping2[str] = pattern[i]
		}
	}
	return true
}
