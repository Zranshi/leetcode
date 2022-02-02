package main

import "fmt"

// @Time     : 2022/01/30 13:39
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 037. 小行星碰撞

func asteroidCollision(asteroids []int) (ans []int) {
	for i := 0; i < len(asteroids); i++ {
		// 当前星球向左飞的时候
		if asteroids[i] < 0 {
			existFlag := true                         // 向左飞的星球是否还存在
			for len(ans) > 0 && ans[len(ans)-1] > 0 { // 如果当前栈中无元素，或者都是向左飞的星球，则加入当前星球
				idxPlant := ans[len(ans)-1]
				if idxPlant+asteroids[i] > 0 {
					existFlag = false
					break
				} else if idxPlant+asteroids[i] < 0 {
					ans = ans[:len(ans)-1]
				} else {
					ans = ans[:len(ans)-1]
					existFlag = false
					break
				}
			}
			// 如果还存在，说明会一直存在，直接加入ans
			if existFlag {
				ans = append(ans, asteroids[i])
			}

		} else { // 当前星球向右飞的时候
			ans = append(ans, asteroids[i])
		}
	}
	return
}

func main() {
	fmt.Println(asteroidCollision([]int{-2, 10, 2, -8, -11}))
}
