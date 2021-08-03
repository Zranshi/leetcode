package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/7/18 11:07
// @Author   : Ranshi
// @File     : main.go

func groupAnagrams(strs []string) [][]string {
	mapping := map[string][]string{}
	for i := range strs {
		s := []byte(strs[i])
		sort.Slice(s, func(i, j int) bool {
			return s[i] < s[j]
		})
		flag := string(s)
		mapping[flag] = append(mapping[flag], strs[i])
	}
	var res [][]string
	for key := range mapping {
		res = append(res, mapping[key])
	}
	return res
}

func main() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}
