package main

func findDisappearedNumbers(nums []int) []int {
	length := len(nums)
	for _, item := range nums {
		nums[(item-1)%length] += length
	}
	var ret []int
	for i, num := range nums {
		if num <= length {
			ret = append(ret, i+1)
		}
	}
	return ret
}
