class Calculadora:
    def somar(self, *args):
        return sum(args)


def main():
    calc = Calculadora()

     
    soma_2 = calc.somar(5, 10)
    print(f"Soma de 5 e 10: {soma_2}")

    
    soma_3 = calc.somar(5, 10, 15)
    print(f"Soma de 5, 10 e 15: {soma_3}")


if __name__ == "__main__":
    main()

    