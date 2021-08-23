package main

import "fmt"

// @Time     : 2021/08/23 10:03
// @Author   : Ranshi
// @File     : main.go
func findSmallestSetOfVertices(n int, edges [][]int) []int {
	// 找到所有入度为 0 的点
	endPointsMap := make(map[int]bool)
	res := make([]int, 0)

	for i := 0; i < len(edges); i++ {
		if _, ok := endPointsMap[edges[i][1]]; !ok {
			endPointsMap[edges[i][1]] = true
		}
	}

	// fmt.Println(endPointsMap)

	for i := 0; i < n; i++ {
		if _, ok := endPointsMap[i]; !ok {
			res = append(res, i)
		}
	}

	return res
}

func main() {
	fmt.Println(findSmallestSetOfVertices(6, [][]int{
		{0, 1},
		{0, 2},
		{2, 5},
		{3, 4},
		{4, 2},
	}))
}
