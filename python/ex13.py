class Matematica:
    @staticmethod
    def fatorial(n):
        if n < 0:
            raise ValueError("O fatorial não está definido para números negativos.")
        elif n == 0 or n == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, n + 1):
                resultado *= i
            return resultado

def main():
    numero = 5
    fatorial_resultado = Matematica.fatorial(numero)
    print(f"O fatorial de {numero} é: {fatorial_resultado}")

    
    try:
        fatorial_negativo = Matematica.fatorial(-3)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
