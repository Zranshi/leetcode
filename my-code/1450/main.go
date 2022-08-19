package main

import "fmt"

// @Time     : 2022/08/19 17:02
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1450. 在既定时间做作业的学生人数

func busyStudent(startTime []int, endTime []int, queryTime int) (ans int) {
	for i := range startTime {
		if startTime[i] <= queryTime && endTime[i] >= queryTime {
			ans++
		}
	}
	return ans
}

func main() {
	fmt.Println(busyStudent([]int{1, 2, 3}, []int{3, 2, 7}, 4))
}
