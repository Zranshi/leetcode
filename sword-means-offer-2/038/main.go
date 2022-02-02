package main

import "fmt"

// @Time     : 2022/01/30 15:01
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 038. 每日温度

func dailyTemperatures(temperatures []int) []int {
	ans := make([]int, len(temperatures))
	for i := len(ans) - 2; i >= 0; i-- {
		idx := 1
		for {
			if temperatures[i+idx] > temperatures[i] {
				ans[i] = idx
				break
			} else {
				if ans[i+idx] == 0 {
					ans[i] = 0
					break
				}
				idx += ans[i+idx]
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(dailyTemperatures([]int{73, 74, 75, 71, 69, 72, 76, 73}))
}
