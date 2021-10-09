package main

import "fmt"

// @Time     : 2021/10/07 11:34
// @Author   : Ranshi
// @File     : main.go

func countSegments(s string) (ans int) {
	for i, ch := range s {
		if (i == 0 || s[i-1] == ' ') && ch != ' ' {
			ans++
		}
	}
	return
}

func main() {
	fmt.Println(countSegments("Hello, my name is John"))
}
