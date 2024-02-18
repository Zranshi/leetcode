package main

import "fmt"

func minimumTimeToInitialState(word string, k int) int {
	pre := make([]string, len(word))
	for i := 0; i < len(word); i++ {
		pre[i] = word[:i+1]
	}
	res, left := 1, k
	for left < len(word) {
		subWord := word[left:]
		if pre[len(subWord)-1] == subWord {
			break
		}
		res, left = res+1, left+k
	}
	return res
}

func main() {
	fmt.Println(minimumTimeToInitialState("abcbabcd", 2))
}
