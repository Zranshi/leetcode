package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/01/24 21:06
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 033. 变位词组

func groupAnagrams(strs []string) [][]string {
	strMapping := make(map[string][]string, 0)
	for _, s := range strs {
		keyBytes := []byte(s)
		sort.Slice(keyBytes, func(i, j int) bool {
			return keyBytes[i] < keyBytes[j]
		})
		key := string(keyBytes)
		strMapping[key] = append(strMapping[key], s)
	}
	res := [][]string{}
	for _, v := range strMapping {
		res = append(res, v)
	}
	return res
}

func main() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}
