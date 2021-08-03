package main

import (
	"strconv"
	"strings"
)

// @Time     : 2021/5/31 15:08
// @Author   : Ranshi
// @File     : 383. 赎金信.go

// 哈希表
func _canConstruct(ransomNote string, magazine string) bool {
	charMap := make(map[byte]int)
	for i := range magazine {
		if _, ok := charMap[magazine[i]]; ok {
			charMap[magazine[i]]++
		} else {
			charMap[magazine[i]] = 1
		}
	}
	for i := range ransomNote {
		if _, ok := charMap[ransomNote[i]]; ok {
			if charMap[ransomNote[i]] == 0 {
				return false
			}
			charMap[ransomNote[i]]--
		} else {
			return false
		}
	}
	return true
}

// strings.Count 函数
func canConstruct(ransomNote string, magazine string) bool {
	for i := 0; i < 26; i++ {
		char := strconv.Itoa('a' + i)
		if strings.Count(ransomNote, char) > strings.Count(magazine, char) {
			return false
		}
	}
	return true
}
