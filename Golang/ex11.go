package main

import (
	"fmt"
)

type Funcionario interface {
	CalcularSalario() float64
}

type FuncionarioHorista struct {
	HorasTrabalhadas float64
	ValorHora        float64
}

func (f FuncionarioHorista) CalcularSalario() float64 {
	return f.HorasTrabalhadas * f.ValorHora
}

type FuncionarioAssalariado struct {
	SalarioMensal float64
}

func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.SalarioMensal
}

func ExibirSalario(funcionario Funcionario) {
	fmt.Printf("Salário: %.2f\n", funcionario.CalcularSalario())
}

func main() {
	funcionario1 := FuncionarioHorista{HorasTrabalhadas: 40, ValorHora: 15.0}
	funcionario2 := FuncionarioAssalariado{SalarioMensal: 3000.0}

	ExibirSalario(funcionario1)
	ExibirSalario(funcionario2)
}
