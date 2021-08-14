package main

// @Time     : 2021/5/31 10:14
// @Author   : Ranshi
// @File     : 344. 反转字符串.go

func reverseString(s []byte) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

func main() {
}
