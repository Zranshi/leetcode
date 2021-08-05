package main

import "fmt"

// @Time     : 2021/08/05 09:30
// @Author   : Ranshi
// @File     : main.go

func eventualSafeNodes(graph [][]int) (res []int) {
	color := make([]int, len(graph))
	var safe func(x int) bool
	safe = func(x int) bool {
		if color[x] > 0 {
			return color[x] == 2
		}
		color[x] = 1
		for y := range graph[x] {
			if !safe(graph[x][y]) {
				return false
			}
		}
		color[x] = 2
		return true
	}
	for i := 0; i < len(graph); i++ {
		if safe(i) {
			res = append(res, i)
		}
	}
	return
}

func main() {
	fmt.Println(eventualSafeNodes([][]int{
		{1, 2},
		{2, 3},
		{5},
		{0},
		{5},
		{},
		{},
	}))
}
