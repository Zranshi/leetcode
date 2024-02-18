package main

import "fmt"

func divisorGame(n int) bool {
	dp := make([]bool, n+1)
    // 对于数 i, 如果它有因数j能够使得 dp[i-j] == false, 则说明alice可以通过这种方法获得胜利. 因此可以以此类推到n
	dp[1] = false
	for i := 2; i <= n; i++ {
		for j := 1; j < i; j++ {
			if i%j == 0 && !dp[i-j] {
				dp[i] = true
				break
			}
		}
	}
	return dp[n]
}

func main() {
	fmt.Println(divisorGame(3))
}
