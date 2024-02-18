package main

import "fmt"

func maximalSquare(matrix [][]byte) (ans int) {
	row, col := len(matrix), len(matrix[0])
	dp := make([][]int, row)
	for i := 0; i < row; i++ {
		dp[i] = make([]int, col)
	}
	for i := 0; i < row; i++ {
		if matrix[i][0] == '1' {
			dp[i][0] = 1
		}
	}
	for i := 0; i < col; i++ {
		if matrix[0][i] == '1' {
			dp[0][i] = 1
		}
	}
	for i := 1; i < row; i++ {
		for j := 1; j < col; j++ {
            if matrix[i][j] == '1' {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            }
		}
	}
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			ans = max(ans, dp[i][j]*dp[i][j])
		}
	}
    return ans
}

func main() {
	fmt.Println(maximalSquare([][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '1', '1', '1'},
		{'1', '1', '1', '1', '1'},
		{'1', '0', '1', '1', '1'},
	}))
}

// 1 1 1 1 0
// 1 2 2 2 1
// 1 2 3 3 2
// 1 0 1 2 3
