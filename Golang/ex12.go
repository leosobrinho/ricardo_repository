package main

import (
	"fmt"
)

type Produto struct {
	Nome  string
	Preco float64
}

func SomarProdutos(p1, p2 Produto) Produto {
	return Produto{
		Nome:  p1.Nome + " e " + p2.Nome,
		Preco: p1.Preco + p2.Preco,
	}
}

func main() {
	produto1 := Produto{Nome: "Produto A", Preco: 30.50}
	produto2 := Produto{Nome: "Produto B", Preco: 20.75}

	resultado := SomarProdutos(produto1, produto2)

	fmt.Printf("Produto: %s\nPreço Total: %.2f\n", resultado.Nome, resultado.Preco)
}
