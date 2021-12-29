package main

import "fmt"

// @Time     : 2021/12/15 08:00
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 851. 喧闹和富有

func loudAndRich(richer [][]int, quiet []int) []int {
	n := len(quiet)
	g := make([][]int, n)
	inDeg := make([]int, n)
	for _, r := range richer {
		g[r[0]] = append(g[r[0]], r[1])
		inDeg[r[1]]++
	}

	ans := make([]int, n)
	for i := range ans {
		ans[i] = i
	}
	q := make([]int, 0, n)
	for i, deg := range inDeg {
		if deg == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		for _, y := range g[x] {
			if quiet[ans[x]] < quiet[ans[y]] {
				ans[y] = ans[x]
			}
			inDeg[y]--
			if inDeg[y] == 0 {
				q = append(q, y)
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(loudAndRich([][]int{
		{1, 0},
		{2, 1},
		{3, 1},
		{3, 7},
		{4, 3},
		{5, 3},
		{6, 3},
	}, []int{3, 2, 5, 4, 6, 1, 7, 0}))
}
