package main

import "math"

// @Time     : 2021/6/1 16:53
// @Author   : Ranshi
// @File     : 8. 字符串转换整数 (atoi).go
func myAtoi(s string) int {
	abs, sign, i, n := 0, 1, 0, len(s)
	for i < n && s[i] == ' ' {
		i++
	}
	if i < n {
		if s[i] == '-' {
			sign = -1
			i++
		} else if s[i] == '+' {
			sign = 1
			i++
		}
	}
	for i < n && s[i] >= '0' && s[i] <= '9' {
		abs = 10*abs + int(s[i]-'0')
		if sign*abs < math.MinInt32 {
			return math.MinInt32
		} else if sign*abs > math.MaxInt32 {
			return math.MaxInt32
		}
		i++
	}
	return sign * abs
}

func main() {

}
