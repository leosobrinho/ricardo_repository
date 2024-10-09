from abc import ABC, abstractmethod


class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Relatorio(Imprimivel):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def imprimir(self):
        print(f"Imprimindo Relatório: {self.conteudo}")


class Contrato(Imprimivel):
    def __init__(self, partes):
        self.partes = partes

    def imprimir(self):
        print(f"Imprimindo Contrato entre: {', '.join(self.partes)}")


def main():
    relatorio = Relatorio("Análise de Desempenho 2024")
    contrato = Contrato(["Empresa A", "Empresa B"])

    
    relatorio.imprimir()
    contrato.imprimir()


if __name__ == "__main__":
    main()
