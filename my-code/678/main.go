package main

import "fmt"

// @Time     : 2021/09/12 00:09
// @Author   : Ranshi
// @File     : main.go

func checkValidString(s string) bool {
	minCount, maxCount := 0, 0
	for _, ch := range s {
		if ch == '(' {
			minCount++
			maxCount++
		} else if ch == ')' {
			minCount = max(minCount-1, 0)
			maxCount--
			if maxCount < 0 {
				return false
			}
		} else {
			minCount = max(minCount-1, 0)
			maxCount++
		}
	}
	return minCount == 0
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	fmt.Println(checkValidString("(*)"))
}
