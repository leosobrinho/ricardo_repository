package main

import (
	"fmt"
)

type Imprimível interface {
	Imprimir()
}

type Relatório struct {
	Título   string
	Conteúdo string
}

func (r Relatório) Imprimir() {
	fmt.Printf("Relatório: %s\nConteúdo: %s\n", r.Título, r.Conteúdo)
}

type Contrato struct {
	Partes string
	Termos string
}

func (c Contrato) Imprimir() {
	fmt.Printf("Contrato entre: %s\nTermos: %s\n", c.Partes, c.Termos)
}

func ImprimirDocumento(i Imprimível) {
	i.Imprimir()
}

func main() {
	relatorio := Relatório{Título: "Relatório Anual", Conteúdo: "Este é o conteúdo do relatório anual."}
	contrato := Contrato{Partes: "Empresa A e Empresa B", Termos: "Os termos do contrato são..."}

	ImprimirDocumento(relatorio)
	ImprimirDocumento(contrato)
}
