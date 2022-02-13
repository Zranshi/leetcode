package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/2/7 10:00
// @Author   : rs
// @File     : main.go

func longestDiverseString(a int, b int, c int) string {
	var ans []byte
	cnt := []struct {
		c  int
		ch byte
	}{
		{a, 'a'},
		{b, 'b'},
		{c, 'c'},
	}
	for {
		sort.Slice(cnt, func(i, j int) bool {
			return cnt[i].c > cnt[j].c
		})
		hasNext := false
		for i, p := range cnt {
			if p.c <= 0 {
				break
			}
			m := len(ans)
			if m >= 2 && ans[m-2] == p.ch && ans[m-1] == p.ch {
				continue
			}
			hasNext = true
			ans = append(ans, p.ch)
			cnt[i].c--
			break
		}
		if !hasNext {
			return string(ans)
		}
	}
}

func main() {
	fmt.Println(longestDiverseString(1, 1, 7))
}
