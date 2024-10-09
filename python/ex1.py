
class Car:
    def __init__(self, marca, modelo , ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def display_details(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"
    

def main():
    carro1 = Car("Toyota", "Corolla", 2024)
    carro2 = Car("BMW", "X6", 2023)
    carro3 = Car("Chevrolet", "Montana", 2015)

    print(carro1.display_details())
    print(carro2.display_details())
    print(carro3.display_details())


if __name__ == "__main__":
    main()

