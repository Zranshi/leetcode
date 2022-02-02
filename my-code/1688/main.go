package main

import "fmt"

// @Time     : 2022/01/25 10:24
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1688. 比赛中的配对次数
func numberOfMatches(n int) int {
	return n - 1
}

func main() {
	fmt.Println(numberOfMatches(14))
}
