package main

// Trie 字典树结构
type Trie struct {
	size   int
	isWord bool
	next   [26]*Trie
}

// Insert 插入一个新的字符串
func (t *Trie) Insert(word string) {
	if len(word) == 0 {
		return
	}
	cur := t
	for i := range word {
		if cur.next[word[i]-'a'] == nil {
			cur.next[word[i]-'a'] = new(Trie)
		}
		cur = cur.next[word[i]-'a']
	}
	if !cur.isWord {
		cur.isWord = true
		t.size++
	}
}

// Search 搜索是否存在当前字符串
func (t *Trie) Search(word string) bool {
	length := len(word)
	if length == 0 {
		return false
	}
	cur := t
	for i := 0; i < length; i++ {
		if cur = cur.next[word[i]-'a']; cur == nil {
			return false
		}
	}
	return cur.isWord
}

// StartsWith 搜索是否存在以当前字符串开头的字符串
func (t *Trie) StartsWith(prefix string) bool {
	length := len(prefix)
	if length == 0 {
		return true
	}
	cur := t
	for i := 0; i < length; i++ {
		if cur = cur.next[prefix[i]-'a']; cur == nil {
			return false
		}
	}
	return true
}
