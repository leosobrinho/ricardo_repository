from abc import ABC, abstractmethod


class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_por_hora):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora


class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, salario_mensal):
        self.nome = nome
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal


def main():
    funcionario_horista = FuncionarioHorista("Carlos", 40, 15)  # 40 horas trabalhadas a R$15/h
    funcionario_assalariado = FuncionarioAssalariado("Ana", 3000)  # Salário fixo de R$3000

    
    print(f"Salário do {funcionario_horista.nome}: R${funcionario_horista.calcular_salario():.2f}")
    print(f"Salário da {funcionario_assalariado.nome}: R${funcionario_assalariado.calcular_salario():.2f}")


if __name__ == "__main__":
    main()
