package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func findMinDifference(timePoints []string) int {
	times := make([]int, len(timePoints))
	for i, s := range timePoints {
		time := strings.Split(s, ":")
		hour, _ := strconv.Atoi(time[0])
		minute, _ := strconv.Atoi(time[1])
		times[i] = hour*60 + minute
	}
	sort.Ints(times)
	res := times[0] + 60*24 - times[len(times)-1]
	for i := 0; i < len(times)-1; i++ {
		diff := times[i+1] - times[i]
		if diff < res {
			res = diff
		}
	}
	return res
}

func main() {
	fmt.Println(findMinDifference([]string{"23:59", "00:00"}))
}
