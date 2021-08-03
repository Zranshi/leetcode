package main

import (
	"container/list"
	"fmt"
)

// @Time     : 2021/6/23 13:16
// @Author   : Ranshi
// @File     : 1109. 航班预订统计.go
func corpFlightBookings1(bookings [][]int, n int) []int {
	plants := make([]int, n)
	for _, item := range bookings {
		for i := item[0] - 1; i <= item[1]-1; i++ {
			plants[i] += item[2]
		}
	}
	l := list.New()
	l.PushBack("canon")
	return plants
}

// 差分数组
func corpFlightBookings(bookings [][]int, n int) []int {
	diff, plants := make([]int, n+2), make([]int, n)
	for _, item := range bookings {
		diff[item[0]] += item[2]
		diff[item[1]+1] += -item[2]
	}
	plants[0] = diff[1]
	for i := 1; i < n; i++ {
		plants[i] = plants[i-1] + diff[i+1]
	}
	return plants
}

func main() {
	bookings := [][]int{
		{1, 2, 10},
		{2, 3, 20},
		{2, 5, 25},
	}
	fmt.Println(corpFlightBookings(bookings, 5))
}
