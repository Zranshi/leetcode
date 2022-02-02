package main

import (
	"fmt"
	"strconv"
)

// @Time     : 2022/01/30 10:58
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 036. 后缀表达式

func evalRPN(tokens []string) int {
	stk := []int{}
	for i := 0; i < len(tokens); i++ {
		switch tokens[i] {
		case "+":
			stk[len(stk)-2] = stk[len(stk)-2] + stk[len(stk)-1]
			stk = stk[:len(stk)-1]
		case "-":
			stk[len(stk)-2] = stk[len(stk)-2] - stk[len(stk)-1]
			stk = stk[:len(stk)-1]
		case "*":
			stk[len(stk)-2] = stk[len(stk)-2] * stk[len(stk)-1]
			stk = stk[:len(stk)-1]
		case "/":
			stk[len(stk)-2] = stk[len(stk)-2] / stk[len(stk)-1]
			stk = stk[:len(stk)-1]
		default:
			value, _ := strconv.Atoi(tokens[i])
			stk = append(stk, value)
		}
	}
	return stk[0]
}

func main() {
	fmt.Println(evalRPN([]string{"4", "13", "5", "/", "+"}))
}
