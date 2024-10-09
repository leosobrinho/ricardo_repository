package main

import (
	"fmt"
)

type Animal interface {
	Som() string
}

type Cachorro struct{}

func (c Cachorro) Som() string {
	return "Au Au"
}

type Gato struct{}

func (g Gato) Som() string {
	return "Miau"
}

func FazerSom(a Animal) {
	fmt.Println(a.Som())
}

func main() {
	var cachorro Animal = Cachorro{}
	var gato Animal = Gato{}

	FazerSom(cachorro)
	FazerSom(gato)
}
