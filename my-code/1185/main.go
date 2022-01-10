package main

import "fmt"

// @Time     : 2022/01/03 23:19
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1185. 一周中的第几天

var week = []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
var monthDays = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30}

func dayOfTheWeek(day, month, year int) string {
	days := 0
	days += 365*(year-1971) + (year-1969)/4
	for _, d := range monthDays[:month-1] {
		days += d
	}
	if month >= 3 && (year%400 == 0 || year%4 == 0 && year%100 != 0) {
		days++
	}
	days += day
	return week[(days+3)%7]
}

func main() {
	fmt.Println(dayOfTheWeek(31, 8, 2019))
}
