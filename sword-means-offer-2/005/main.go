package main

import "fmt"

// @Time     : 2021/12/14 22:34
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 005. 单词长度的最大乘积

func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxProduct(words []string) (ans int) {
	n := len(words)
	masksMap := make(map[int]int)
	for i := 0; i < n; i++ {
		bitMask := 0
		for _, c := range words[i] {
			bitMask |= (1 << (c - 'a'))
		}
		if len(words[i]) > masksMap[bitMask] {
			masksMap[bitMask] = len(words[i])
		}
	}

	for x := range masksMap {
		for y := range masksMap {
			if (x & y) == 0 {
				length := masksMap[x] * masksMap[y]
				ans = maxInt(length, ans)
			}
		}
	}
	return
}

func main() {
	fmt.Println(maxProduct([]string{"abcw", "baz", "foo", "bar", "fxyz", "abcdef"}))
}
