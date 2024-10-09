package main

import (
	"fmt"
)

type ContaBancaria struct {
	titular string
	saldo   float64
}

func (c *ContaBancaria) Depositar(valor float64) {
	if valor > 0 {
		c.saldo += valor
	}
}

func (c *ContaBancaria) Sacar(valor float64) bool {
	if valor > 0 && valor <= c.saldo {
		c.saldo -= valor
		return true
	}
	return false
}

func (c ContaBancaria) ObterSaldo() float64 {
	return c.saldo
}

func main() {
	conta1 := ContaBancaria{titular: "João"}
	conta2 := ContaBancaria{titular: "Maria"}

	conta1.Depositar(500)
	conta2.Depositar(300)

	fmt.Printf("Saldo de %s: %.2f\n", conta1.titular, conta1.ObterSaldo())
	fmt.Printf("Saldo de %s: %.2f\n", conta2.titular, conta2.ObterSaldo())

	if conta1.Sacar(200) {
		fmt.Printf("Saque de 200 realizado com sucesso.\n")
	} else {
		fmt.Printf("Saque de 200 não pode ser realizado.\n")
	}

	fmt.Printf("Saldo de %s após o saque: %.2f\n", conta1.titular, conta1.ObterSaldo())
}
