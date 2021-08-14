package main

import "fmt"

// @Time     : 2021/08/10 09:34
// @Author   : Ranshi
// @File     : main.go
func reverse(s []byte) []byte {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func addStrings(num1 string, num2 string) string {
	res := []byte{}
	length1, length2 := len(num1), len(num2)
	arr1, arr2 := reverse([]byte(num1)), reverse([]byte(num2))
	var flag byte = 0
	for i := 0; i < length1 || i < length2; i++ {
		idx := flag
		if i < length1 {
			idx += arr1[i] - '0'
		}
		if i < length2 {
			idx += arr2[i] - '0'
		}
		idx, flag = idx%10, idx/10
		fmt.Println(idx, flag)
		res = append(res, idx+'0')
	}
	if flag != 0 {
		res = append(res, flag+'0')
	}
	return string(reverse(res))
}

func main() {
	fmt.Println(addStrings("78956875673456313252431231243415234123",
		"78956875673456313252431231243415234123"))
}
