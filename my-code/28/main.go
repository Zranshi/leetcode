package main

func strStr(haystack string, needle string) int {
	length, l := len(haystack), len(needle)
	for i := 0; i < length-l+1; i++ {
		if needle == haystack[i:i+l] {
			return i
		}
	}
	return -1
}
