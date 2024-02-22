package main

import "fmt"

type node struct {
	word string
	step int
}

// O(1)
func hasPath(word1, word2 string) bool {
	diffCount := 0
	for i := 0; i < len(word1); i++ {
		if word1[i] != word2[i] {
			diffCount++
		}
		if diffCount > 1 {
			return false
		}
	}
	return diffCount == 1
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	shortest := make([]int, len(wordList))
	queue := []*node{{word: beginWord, step: 1}}
	for len(queue) != 0 {
		idxNode := queue[0]
		for i, word := range wordList {
			if shortest[i] != 0 {
				continue
			}
			if hasPath(word, idxNode.word) {
				if word == endWord {
					return idxNode.step + 1
				}
				queue = append(queue, &node{word, idxNode.step + 1})
				shortest[i] = idxNode.step + 1
			}
		}
		queue = queue[1:]
	}
	return 0
}

func main() {
	fmt.Println(ladderLength("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"}))
}
