package main

import "fmt"

func main() {
	fibSequence := []int{0, 1}
	lastNumber := 1
	i := 2
	for {
		lastNumber = fibSequence[i-1] + fibSequence[i-2]
		if lastNumber > 4000000 {
			break
		}
		fibSequence = append(fibSequence, lastNumber)
		i++
	}
	sum := 0
	for _, x := range fibSequence {
		if x%2 == 0 {
			sum += x
		}
	}
	fmt.Println(sum)
}
