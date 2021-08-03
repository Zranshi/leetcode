package main

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func characterReplacement(s string, k int) int {
	left, right, length, maxLen := 0, 0, len(s), 0
	chars := [26]int{}
	for right < length {
		chars[s[right]-'A']++
		maxLen = MaxInt(maxLen, chars[s[right]-'A'])
		if right-left+1-maxLen > k {
			chars[s[left]-'A']--
			left++
		}
		right++
	}
	return right - left
}
