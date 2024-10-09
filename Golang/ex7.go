package main

import (
	"fmt"
)

type Professor struct {
	Nome        string
	Disciplinas []string
}

type Escola struct {
	Nome        string
	Professores []*Professor // Lista de ponteiros para Professores
}

func (e *Escola) AdicionarProfessor(p *Professor) {
	e.Professores = append(e.Professores, p)
}

func (p *Professor) Lecionar() {
	fmt.Printf("Professor %s leciona as disciplinas: %v\n", p.Nome, p.Disciplinas)
}

func main() {
	escola1 := Escola{Nome: "Escola A"}
	escola2 := Escola{Nome: "Escola B"}

	professor1 := &Professor{Nome: "Carlos", Disciplinas: []string{"Matemática", "Física"}}
	professor2 := &Professor{Nome: "Maria", Disciplinas: []string{"Português", "Literatura"}}
	professor3 := &Professor{Nome: "João", Disciplinas: []string{"Química", "Biologia"}}

	escola1.AdicionarProfessor(professor1)
	escola1.AdicionarProfessor(professor2)

	escola2.AdicionarProfessor(professor2)
	escola2.AdicionarProfessor(professor3)

	fmt.Printf("Professores da %s:\n", escola1.Nome)
	for _, prof := range escola1.Professores {
		prof.Lecionar()
	}

	fmt.Printf("\nProfessores da %s:\n", escola2.Nome)
	for _, prof := range escola2.Professores {
		prof.Lecionar()
	}
}
