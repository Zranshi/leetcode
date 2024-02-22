package main

import "fmt"

func totalNQueens(n int) (ans int) {
	col := make([]bool, n)
	row := make([]bool, n)
	inc := make([]bool, n*2)
	red := make([]bool, n*2)
	isOccupied := func(x, y int) bool {
		return col[y] || row[x] || inc[y-x+n] || red[x+y]
	}
	set := func(x, y int, mark bool) {
		col[y] = mark
		row[x] = mark
		inc[y-x+n] = mark
		red[x+y] = mark
	}
	var dfs func(int)
	dfs = func(i int) {
		if i == n {
			ans++
            return
		}
		for j := 0; j < n; j++ {
			if !isOccupied(i, j) {
				set(i, j, true)
				dfs(i + 1)
				set(i, j, false)
			}
		}
	}
	dfs(0)
	return
}

func main() {
	fmt.Println(totalNQueens(4))
}

// x = y
// 8 = y-x+8
