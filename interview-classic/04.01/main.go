package main

import "fmt"

// @Time     : 2021/6/29 19:33
// @Author   : Ranshi
// @File     : main.go

func findWhetherExistsPath(n int, graph [][]int, start int, target int) bool {
	queue := []int{start}
	path := make([]bool, n)
	path[start] = true
	mapping := map[int][]int{}
	for i := range graph {
		mapping[graph[i][0]] = append(mapping[graph[i][0]], graph[i][1])
	}
	for len(queue) != 0 {
		idx := queue[0]
		if idx == target {
			break
		}
		if val, ok := mapping[idx]; len(val) != 0 && ok {
			for next := range val {
				if !path[val[next]] {
					queue = append(queue, val[next])
					path[val[next]] = true
				}
			}
		}
		queue = queue[1:]
	}
	if len(queue) != 0 {
		return true
	}
	return false
}

func main() {
	fmt.Println(findWhetherExistsPath(3, [][]int{{0, 1}, {0, 2}, {1, 2}, {1, 2}}, 0, 2))
}
