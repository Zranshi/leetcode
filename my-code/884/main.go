package main

import (
	"fmt"
	"strings"
)

// @Time     : 2022/01/30 10:18
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 884. 两句话中的不常见单词

func uncommonFromSentences(s1 string, s2 string) (res []string) {
	wordSet := map[string]bool{}

	wordFromSentences := func(s string) {
		for _, word := range strings.Split(s, " ") {
			if _, ok := wordSet[word]; ok {
				wordSet[word] = false
			} else {
				wordSet[word] = true
			}
		}
	}
	wordFromSentences(s1)
	wordFromSentences(s2)

	for key, value := range wordSet {
		if value {
			res = append(res, key)
		}
	}
	return
}

func main() {
	fmt.Println(uncommonFromSentences("this apple is sweet", "this apple is sour"))
}
