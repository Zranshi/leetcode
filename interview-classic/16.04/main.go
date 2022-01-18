package main

import "fmt"

// @Time     : 2022/01/15 10:28
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 面试题 16.04. 井字游戏

func tictactoe(board []string) string {
	N := len(board)
	winner, finish := uint8(' '), true
	// 检查行
	for i := 0; i < N; i++ {
		winner = board[i][0]
		for j := 0; j < N; j++ {
			if j > 0 && board[i][j] != board[i][j-1] {
				winner = ' '
			}
			if board[i][j] == ' ' {
				finish = false
				break
			}
		}
		if winner != ' ' {
			return string(winner)
		}
	}

	// 检查列
	for i := 0; i < N; i++ {
		winner = board[0][i]
		for j := 1; j < N; j++ {
			if board[j][i] != board[j-1][i] {
				winner = ' '
			}
		}
		if winner != ' ' {
			return string(winner)
		}
	}

	//检查左上到右下的对角线
	winner = board[0][0]
	for i := 0; i < N-1; i++ {
		if board[i][i] != board[i+1][i+1] {
			winner = ' '
			break
		}
	}
	if winner != ' ' {
		return string(winner)
	}

	//检查左下到右上的对角线
	winner = board[N-1][0]
	for i := N - 1; i > 0; i-- {
		if board[i][N-1-i] != board[i-1][N-i] {
			winner = ' '
			break
		}
	}
	if winner != ' ' {
		return string(winner)
	}

	if finish {
		return "Draw"
	}
	return "Pending"
}

func main() {
	fmt.Println(tictactoe([]string{
		"O X",
		" XO",
		"X O",
	},
	))
}
