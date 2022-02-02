package main

import "fmt"

// @Time     : 2022/02/02 09:37
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 2000. 反转单词前缀

func reversePrefix(word string, ch byte) string {
	index := 0
	wordBytes := []byte(word)
	for i := 0; i < len(wordBytes); i++ {
		if wordBytes[i] == ch {
			index = i
			break
		}
	}
	for i, j := 0, index; i < j; i, j = i+1, j-1 {
		wordBytes[i], wordBytes[j] = wordBytes[j], wordBytes[i]
	}
	return string(wordBytes)
}

func main() {
	fmt.Println(reversePrefix("abcdefd", 'd'))
}
