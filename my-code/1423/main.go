package main

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxScore(cardPoints []int, k int) int {
	res, idx, length := 0, 0, len(cardPoints)
	for i := 0; i < k; i++ {
		res += cardPoints[i]
	}
	ans := res
	for idx < k {
		ans = ans - cardPoints[k-idx-1] + cardPoints[length-idx-1]
		res = MaxInt(res, ans)
		idx++
	}
	return res
}
