package main

import "fmt"

// @Time     : 2021/09/10 17:57
// @Author   : Ranshi
// @File     : main.go

func countEval(s string, result int) int {
	dp := make([][][2]int, len(s))
	for i := 0; i < len(dp); i++ {
		dp[i] = make([][2]int, len(s))
	}
	//dp[0][len-1][result]即为答案，i需要倒序遍历，j正序遍历
	for i := len(s) - 1; i >= 0; i -= 2 {
		for j := i; j < len(s); j += 2 {
			if i == j {
				if s[i] == '0' {
					dp[i][j][0]++
				} else {
					dp[i][j][1]++
				}
				continue
			}
			for k := i + 1; k < j; k += 2 {
				for arg1 := 0; arg1 <= 1; arg1++ {
					for arg2 := 0; arg2 <= 1; arg2++ {
						if doBoolOp(arg1, arg2, s[k]) == 0 {
							dp[i][j][0] += dp[i][k-1][arg1] * dp[k+1][j][arg2]
						} else {
							dp[i][j][1] += dp[i][k-1][arg1] * dp[k+1][j][arg2]
						}
					}
				}

			}
		}
	}
	return dp[0][len(s)-1][result]
}

func doBoolOp(arg1, arg2 int, operator byte) int {
	if operator == '&' {
		return arg1 & arg2
	} else if operator == '|' {
		return arg1 | arg2
	} else {
		return arg1 ^ arg2
	}
}

func main() {
	fmt.Println(countEval("1^0|0|1", 0))
}
