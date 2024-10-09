package main

import (
	"fmt"
)

type Carro struct {
	Marca      string
	Modelo     string
	Ano        int
	Velocidade int
}

func (c *Carro) Acelerar(quantidade int) {
	c.Velocidade += quantidade
}

func (c *Carro) Frear(quantidade int) {
	if c.Velocidade-quantidade < 0 {
		c.Velocidade = 0
	} else {
		c.Velocidade -= quantidade
	}
}

func (c Carro) ExibirVelocidade() {
	fmt.Printf("A velocidade atual do %s %s é: %d km/h\n", c.Marca, c.Modelo, c.Velocidade)
}

func main() {

	carro1 := Carro{Marca: "Toyota", Modelo: "Corolla", Ano: 2020}
	carro2 := Carro{Marca: "Ford", Modelo: "Focus", Ano: 2019}
	carro3 := Carro{Marca: "Honda", Modelo: "Civic", Ano: 2021}

	carro1.Acelerar(50)
	carro1.ExibirVelocidade()

	carro2.Acelerar(30)
	carro2.ExibirVelocidade()

	carro3.Acelerar(70)
	carro3.ExibirVelocidade()

	carro1.Frear(20)
	carro1.ExibirVelocidade()

	carro2.Frear(50)
	carro2.ExibirVelocidade()

	carro3.Frear(100)
	carro3.ExibirVelocidade()
}
