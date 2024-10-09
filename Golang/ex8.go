package main

import (
	"fmt"
)

type Empregado struct {
	Nome    string
	Cargo   string
	Salario float64
}

type Empresa struct {
	Nome       string
	Empregados []Empregado // Lista de empregados
}

func (e *Empresa) AdicionarEmpregado(emp Empregado) {
	e.Empregados = append(e.Empregados, emp)
}

func (e *Empresa) ExibirEmpregados() {
	fmt.Printf("Empregados da empresa %s:\n", e.Nome)
	for _, emp := range e.Empregados {
		fmt.Printf("Nome: %s, Cargo: %s, Salário: %.2f\n", emp.Nome, emp.Cargo, emp.Salario)
	}
}

func main() {
	empresa := Empresa{Nome: "Tech Solutions"}

	emp1 := Empregado{Nome: "Ana", Cargo: "Desenvolvedora", Salario: 5000.00}
	emp2 := Empregado{Nome: "Bruno", Cargo: "Gerente de Projetos", Salario: 8000.00}
	emp3 := Empregado{Nome: "Carla", Cargo: "Analista de Sistemas", Salario: 6000.00}

	empresa.AdicionarEmpregado(emp1)
	empresa.AdicionarEmpregado(emp2)
	empresa.AdicionarEmpregado(emp3)

	empresa.ExibirEmpregados()
}
