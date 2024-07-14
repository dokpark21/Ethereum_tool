package group

// 곱셈군 집합과 곱셈군의 생성원들을 구하는 함수 만들기
import (
	"fmt"
	"math"
)

func gcd(a, b uint) uint {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func contains(slice []uint, value uint) bool {
	for _, v := range slice {
		if v == value {
			return true
		}
	}
	return false
}

func getMultiplicativeGroup(n uint) (group []uint, generators []uint) {
	// 그룹 생성
	for i := uint(1); i < n; i++ {
		if gcd(i, n) == 1 {
			group = append(group, i)
		}
	}

	// 생성자 구하기
	for _, g := range group {
		mem := make([]uint, 0, len(group))
		for k := uint(0); k < n-1; k++ {
			val := uint(math.Pow(float64(g), float64(k))) % n
			if !contains(mem, val) {
				mem = append(mem, val)
			}
		}
		if len(mem) == len(group) {
			generators = append(generators, g)
		}
	}

	return group, generators
}

func main() {
	n := 130
	group, generators := getMultiplicativeGroup(uint(n))

	fmt.Println("Multiplicative Group of Z", n, ":")
	for _, value := range group {
		if value != 0 {
			fmt.Printf("%d ", value)
		}
	}
	fmt.Println()
	fmt.Println("Generators of Z*", n, ":")
	for _, value := range generators {
		if value != 0 {
			fmt.Printf("%d ", value)
		}

	}
}
