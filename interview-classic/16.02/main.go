package main

// @Time     : 2021/7/22 20:52
// @Author   : Ranshi
// @File     : main.go

type WordsFrequency struct {
	words map[string]int
}

func Constructor(book []string) WordsFrequency {
	m := make(map[string]int, 0)
	for i := range book {
		if _, ok := m[book[i]]; ok {
			m[book[i]]++
		} else {
			m[book[i]] = 1
		}
	}
	return WordsFrequency{words: m}
}

func (f *WordsFrequency) Get(word string) int {
	if res, ok := f.words[word]; ok {
		return res
	} else {
		return 0
	}
}

func main() {

}
