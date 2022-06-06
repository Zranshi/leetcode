package main

import (
	"fmt"
	"sort"
)

func nextGreatestLetter(letters []byte, target byte) byte {
	if target >= letters[len(letters)-1] {
		return letters[0]
	}
	i := sort.Search(len(letters)-1, func(i int) bool {
		return letters[i] > target
	})
	return letters[i]
}

func main() {
	fmt.Println(nextGreatestLetter([]byte{'c', 'f', 'j'}, 'a'))
}
