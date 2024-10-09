package main

import (
	"fmt"
)

type Motor struct {
	Potencia int    // Potência do motor em cavalos de potência (CV)
	Tipo     string // Tipo de motor (ex: "Gasolina", "Álcool", "Elétrico")
}

type Carro struct {
	Marca  string
	Modelo string
	Ano    int
	Motor  Motor // Associando um objeto Motor à classe Carro
}

func main() {
	motor1 := Motor{Potencia: 150, Tipo: "Gasolina"}
	carro1 := Carro{Marca: "Toyota", Modelo: "Corolla", Ano: 2020, Motor: motor1}

	motor2 := Motor{Potencia: 200, Tipo: "Elétrico"}
	carro2 := Carro{Marca: "Tesla", Modelo: "Model 3", Ano: 2021, Motor: motor2}

	fmt.Printf("Carro: %s %s (%d) - Motor: %d CV, Tipo: %s\n", carro1.Marca, carro1.Modelo, carro1.Ano, carro1.Motor.Potencia, carro1.Motor.Tipo)
	fmt.Printf("Carro: %s %s (%d) - Motor: %d CV, Tipo: %s\n", carro2.Marca, carro2.Modelo, carro2.Ano, carro2.Motor.Potencia, carro2.Motor.Tipo)
}
