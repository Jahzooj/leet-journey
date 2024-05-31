package main

import "fmt"

func binary_search(target int, arr []int) int {
	var start int = 0
	var end int = len(arr) - 1
	var mid int

	for start < end {
		mid = (start + end) / 2
		if arr[mid] == target {
			return mid
		} else if target < arr[mid] {
			end = mid
		} else if target > arr[mid] {
			start = mid + 1
		}
	}

	if arr[start] == target {
		return start
	} else {
		return -1
	}
}

func main() {
	arr := []int{1, 2, 5, 6, 7, 9, 12, 15, 18, 20}

	index := binary_search(18, arr)

	fmt.Println("index of the target element is", index)
}