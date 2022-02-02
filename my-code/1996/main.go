package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/01/28 22:06
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1996. 游戏中弱角色的数量
func numberOfWeakCharacters(properties [][]int) (ans int) {
	sort.Slice(properties, func(i, j int) bool {
		p, q := properties[i], properties[j]
		return p[0] > q[0] || p[0] == q[0] && p[1] < q[1]
	})
	maxDef := 0
	for _, p := range properties {
		if p[1] < maxDef {
			ans++
		} else {
			maxDef = p[1]
		}
	}
	return
}

func main() {
	fmt.Println(numberOfWeakCharacters([][]int{
		{1, 5},
		{10, 4},
		{4, 3},
	}))
}
