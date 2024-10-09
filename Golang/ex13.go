package main

import (
	"fmt"
)

type Matematica struct{}

func (Matematica) Fatorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * Matematica{}.Fatorial(n-1)
}

func main() {
	m := Matematica{}
	numero := 5
	resultado := m.Fatorial(numero)
	fmt.Printf("Fatorial de %d é %d\n", numero, resultado)
}
