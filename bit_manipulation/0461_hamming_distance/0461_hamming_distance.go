package main

import (
	"fmt"
)

func hammingDistance(x int, y int) int {
	x ^= y

	res := 0
	for x > 0 {
		res += x & 1
		x >>= 1
	}

	return res
}

func main() {
	var x int = 1
	var y int = 4
	fmt.Println(hammingDistance(x, y))
}
