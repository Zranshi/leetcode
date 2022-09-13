package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/09/13 17:44
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 670. 最大交换

func maximumSwap(num int) int {
	x := num
	numS := []int{}
	for x != 0 {
		numS = append(numS, x%10)
		x /= 10
	} // [6 3 7 2]
	for i, j := 0, len(numS)-1; i < j; i, j = i+1, j-1 {
		numS[i], numS[j] = numS[j], numS[i]
	} // [2 7 3 6]
	sortNum := make([]int, len(numS))
	copy(sortNum, numS)
	sort.Slice(sortNum, func(i, j int) bool {
		return sortNum[i] > sortNum[j]
	}) // [7 6 3 2]

	for i := 0; i < len(numS); i++ {
		if numS[i] < sortNum[i] {
			for j := len(numS) - 1; j > i; j-- {
				if numS[j] == sortNum[i] {
					numS[i], numS[j] = numS[j], numS[i]
					ans := 0
					for _, v := range numS {
						ans *= 10
						ans += v
					}
					return ans
				}
			}
		}
	}
	return num
}

func main() {
	fmt.Println(maximumSwap(9973))
}
