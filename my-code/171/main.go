package main

import "math"

// @Time     : 2021/5/30 07:54
// @Author   : Ranshi
// @File     : 171. Excel表列序号.go
func titleToNumber(columnTitle string) (ans int) {
	for i := 0; i < len(columnTitle); i++ {
		ans += int(columnTitle[i]-'A'+1) * int(math.Pow(26, float64(len(columnTitle)-i-1)))
	}
	return ans
}
