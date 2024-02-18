package main

import (
	"fmt"
	"strconv"
)

func diffWaysToCompute(expression string) []int {
	mem := make(map[string][]int, 0)
	return dfs(expression, mem)
}

func isNumber(expr string) (bool, int) {
	val, err := strconv.Atoi(expr)
	if err != nil {
		return false, -1
	}
	return true, val
}

func dfs(expr string, mem map[string][]int) (ans []int) {
	// 如果当前节点维数字, 则直接返回
	if ok, val := isNumber(expr); ok {
		return []int{val}
	}
	// 使用mem记忆化搜索来简化
	if _, ok := mem[expr]; ok {
		return mem[expr]
	}

	for i := 0; i < len(expr); i++ {
		ch := expr[i]
		if ch == '+' || ch == '-' || ch == '*' {
			left := dfs(expr[:i], mem)
			right := dfs(expr[i+1:], mem)
			val := 0
			for _, leftVal := range left {
				for _, rightVal := range right {
					switch ch {
					case '+':
						val = leftVal + rightVal
					case '-':
						val = leftVal - rightVal
					case '*':
						val = leftVal * rightVal
					}
					ans = append(ans, val)
				}
			}
		}
	}
	mem[expr] = ans
	return ans
}

func main() {
	fmt.Println(diffWaysToCompute("2*3-4*5"))
}
