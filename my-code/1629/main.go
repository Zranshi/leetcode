package main

import "fmt"

// @Time     : 2022/01/09 08:57
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1629. 按键持续时间最长的键

func slowestKey(releaseTimes []int, keysPressed string) byte {
	maxTime := releaseTimes[0]
	res := keysPressed[0]
	for i := 1; i < len(releaseTimes); i++ {
		valTime := releaseTimes[i] - releaseTimes[i-1]
		if valTime > maxTime || valTime == maxTime && keysPressed[i] > res {
			maxTime = valTime
			res = keysPressed[i]
		}
	}
	return res
}

func main() {
	fmt.Println(slowestKey([]int{12, 23, 36, 46, 62}, "spuda"))
}
