

class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_detalhes(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []  

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    def exibir_empregados(self):
        for empregado in self.empregados:
            print(empregado.exibir_detalhes())


def main():
    empresa = Empresa("Tech Solutions")

    
    empregado1 = Empregado("Carlos Silva", "Desenvolvedor", 5000)
    empregado2 = Empregado("Ana Souza", "Gerente de Projetos", 8000)
    empregado3 = Empregado("João Oliveira", "Analista de Sistemas", 6000)

    
    empresa.adicionar_empregado(empregado1)
    empresa.adicionar_empregado(empregado2)
    empresa.adicionar_empregado(empregado3)

    
    print(f"Empregados da empresa {empresa.nome}:")
    empresa.exibir_empregados()


if __name__ == "__main__":
    main()
