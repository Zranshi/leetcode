package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

// @Time     : 2022/01/30 10:29
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 035. 最小时间差

func findMinDifference(timePoints []string) int {
	if len(timePoints) > 1440 {
		return 0
	}
	times := []int{}
	for i := 0; i < len(timePoints); i++ {
		timePoint := strings.Split(timePoints[i], ":")
		hour, _ := strconv.Atoi(timePoint[0])
		minute, _ := strconv.Atoi(timePoint[1])
		time := hour*60 + minute
		times = append(times, time)
	}
	sort.Ints(times)
	minDiff := times[0] + 1440 - times[len(times)-1]
	for i := 1; i < len(times); i++ {
		diff := times[i] - times[i-1]
		if minDiff > diff {
			minDiff = diff
		}
	}
	return minDiff
}

func main() {
	fmt.Println(findMinDifference([]string{"23:59", "00:00"}))
}
