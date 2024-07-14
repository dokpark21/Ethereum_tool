package number_theory

import (
	"fmt"
	"math"
)

func Problem1() (result []int) {
	for i := 0; i < 9; i++ {
		if (3*i)%9 == 6%9 {
			result = append(result, i)
		}
	}

	return result
}

func Problem2() (result []int) {
	for i := 0; i < 37; i++ {
		if (30*i)%37 == 12%37 {
			result = append(result, i)
		}
	}

	return result
}

func Problem3() (result []int) {
	base := math.Pow(13, 123456789)
	fmt.Println(math.Pow(13, 123456789))
	for i := 0; i < 17; i++ {
		if (int(base)%17)%17 == i%17 {
			result = append(result, i)
		}
	}

	return result
}
