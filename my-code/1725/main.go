package main

import "fmt"

// @Time     : 2022/02/04 11:48
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1725. 可以形成最大正方形的矩形数目
func minInts(ints ...int) (ans int) {
	for i := 1; i < len(ints); i++ {
		if ints[ans] > ints[i] {
			ans = i
		}
	}
	return ints[ans]
}

func countGoodRectangles(rectangles [][]int) (ans int) {
	maxLen := 0
	for i := 0; i < len(rectangles); i++ {
		idx := minInts(rectangles[i]...)
		if maxLen < idx {
			maxLen = idx
			ans = 1
		} else if maxLen == idx {
			ans++
		}
	}
    return ans
}

func main() {
	fmt.Println(countGoodRectangles([][]int{
		{5, 8},
		{3, 9},
		{5, 12},
		{16, 5},
	}))
}
