package main

// @Time     : 2021/5/31 10:22
// @Author   : Ranshi
// @File     : 345. 反转字符串中的元音字母.go

func reverseVowels(s string) string {
	oriCheck := map[byte]bool{
		'a': true, 'o': true, 'e': true, 'i': true, 'u': true, 'A': true, 'O': true, 'E': true, 'I': true, 'U': true,
	}
	b := []byte(s)
	for l, r := 0, len(b)-1; l < r; {
		for _, ok := oriCheck[b[r]]; l < r && !ok; ok = oriCheck[b[r]] {
			r--
		}
		for _, ok := oriCheck[b[l]]; l < r && !ok; ok = oriCheck[b[l]] {
			l++
		}
		b[l], b[r] = b[r], b[l]
		l++
		r--
	}
	return string(b)
}
