package main

import (
	"fmt"
)

// @Time     : 2022/01/05 07:52
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1576. 替换所有的问号

func modifyString(s string) string {
	res := []byte(s)
	n := len(res)
	for i, ch := range res {
		if ch == '?' {
			for b := byte('a'); b <= 'c'; b++ {
				if !(i > 0 && res[i-1] == b || i < n-1 && res[i+1] == b) {
					res[i] = b
					break
				}
			}
		}
	}
	return string(res)
}

func main() {
	fmt.Println(modifyString("?zs"))
}
