package main

// @Time     : 2021/5/31 15:26
// @Author   : Ranshi
// @File     : 389. 找不同.go
func findTheDifference(s string, t string) byte {
	var mark int32
	for _, v := range t {
		mark += v
	}
	for _, v := range s {
		mark -= v
	}
	return byte(mark)
}
