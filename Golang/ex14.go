package main

import (
	"fmt"
	"sync"
)

type Configuracao struct {
	Parametro string
}

var instancia *Configuracao
var once sync.Once

func GetConfiguracao() *Configuracao {
	once.Do(func() {
		instancia = &Configuracao{Parametro: "Valor padrão"}
	})
	return instancia
}

func main() {
	config1 := GetConfiguracao()
	fmt.Println("Configuração 1:", config1.Parametro)

	config2 := GetConfiguracao()
	config2.Parametro = "Novo valor"

	fmt.Println("Configuração 1 após alteração:", config1.Parametro)
	fmt.Println("Configuração 2:", config2.Parametro)
}
