package main

import (
	"fmt"
	"strings"
)

// @Time     : 2022/01/06 00:26
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 71. 简化路径

func simplifyPath(path string) string {
	stk := []string{}
	pathSlice := strings.Split(path, "/")
	for _, v := range pathSlice {
		if v == "." || v == "" || v == ".." {
			if v == ".." && len(stk) > 0 {
				stk = stk[:len(stk)-1]
			}
		} else {
			stk = append(stk, v)
		}
	}
	return "/" + strings.Join(stk, "/")
}

func main() {
	fmt.Println(simplifyPath("/home/"))
}
