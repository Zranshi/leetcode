package main

import "fmt"

// @Time     : 2022/01/30 23:26
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 039. 直方图最大矩形面积

func largestRectangleArea(heights []int) int {
	heights = append([]int{-1}, append(heights, 0)...)
	var res int
	var stack []int
	for i, h := range heights {
		for len(stack) > 1 && h < heights[stack[len(stack)-1]] {
			w := i - stack[len(stack)-2] - 1
			res = max(res, heights[stack[len(stack)-1]]*w)
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(largestRectangleArea([]int{2, 4}))
}
