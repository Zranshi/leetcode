package main

func searchMatrix(matrix [][]int, target int) bool {
	length, row := len(matrix)*len(matrix[0]), len(matrix[0])
	left, right := 0, length-1
	for left <= right {
		mid := (right-left)/2 + left
		if matrix[mid/row][mid%row] == target {
			return true
		} else if matrix[mid/row][mid%row] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return false
}
