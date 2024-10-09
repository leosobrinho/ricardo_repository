

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []  

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_professor(self)  

    def exibir_escolas(self):
        return ", ".join([escola.nome for escola in self.escolas])

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []  

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def exibir_professores(self):
        return ", ".join([professor.nome for professor in self.professores])


def main():
    escola1 = Escola("Escola Primária")
    escola2 = Escola("Escola Secundária")

    professor1 = Professor("Carlos")
    professor2 = Professor("Ana")

    
    professor1.adicionar_escola(escola1)
    professor1.adicionar_escola(escola2)
    professor2.adicionar_escola(escola1)

    print(f"{professor1.nome} leciona em: {professor1.exibir_escolas()}")
    print(f"{professor2.nome} leciona em: {professor2.exibir_escolas()}")

   
    print(f"Professores da {escola1.nome}: {escola1.exibir_professores()}")
    print(f"Professores da {escola2.nome}: {escola2.exibir_professores()}")


if __name__ == "__main__":
    main()
