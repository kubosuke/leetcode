package main

import (
	"fmt"
)

func myPow(x float64, n int) float64 {
	var ans float64 = 1
	if n < 0 {
		x = 1 / x
		n *= -1
	}
	for i := 0; i < n; i++ {
		ans *= x
	}
	return ans
}

func main() {
	fmt.Println(myPow(2.10000, 3))
}
