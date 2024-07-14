package main

import (
	"fmt"
	number_theory "upside_homework/crypytography.com/number_theory"
)

func main() {
	result := number_theory.Problem1()

	fmt.Print("Result: ")
	for _, v := range result {
		fmt.Printf("%d ", v)
	}

	result = number_theory.Problem2()
	fmt.Print("Result: ")
	for _, v := range result {
		fmt.Printf("%d ", v)
	}

	fmt.Println()

	result = number_theory.Problem3()
	fmt.Print("Result: ")
	for _, v := range result {
		fmt.Printf("%d ", v)
	}
}
