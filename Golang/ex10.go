package main

import (
	"fmt"
)

type Calculadora struct{}

func (c Calculadora) SomarDoisNumeros(a, b float64) float64 {
	return a + b
}

func (c Calculadora) SomarTresNumeros(a, b, c float64) float64 {
	return a + b + c
}

func main() {
	calculadora := Calculadora{}

	resultado1 := calculadora.SomarDoisNumeros(5.5, 3.2)
	fmt.Printf("Resultado da soma de dois números: %.2f\n", resultado1)

	resultado2 := calculadora.SomarTresNumeros(4.0, 2.5, 1.5)
	fmt.Printf("Resultado da soma de três números: %.2f\n", resultado2)
}
