package main

import (
	"fmt"
	"strconv"
)

// @Time     : 2022/01/08 00:14
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 89. 格雷编码

func grayCode(n int) []int {
	ans := make([]int, 1<<n)
	for i := range ans {
		ans[i] = i>>1 ^ i
	}
	return ans
}

func main() {
	ans := grayCode(5)
	for _, v := range ans {
		fmt.Println(strconv.FormatInt(int64(v), 2))
	}
}
