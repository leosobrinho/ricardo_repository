class Car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  

    def display_details(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

    def accelerate(self, incremento):
        self.velocidade += incremento
        print(f"O carro acelerou {incremento} km/h. Velocidade atual: {self.velocidade} km/h")

    def brake(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)  
        print(f"O carro reduziu {decremento} km/h. Velocidade atual: {self.velocidade} km/h")

    def display_speed(self):
        return f"Velocidade atual: {self.velocidade} km/h"


if __name__ == "__main__":
    carro1 = Car("Toyota", "Corolla", 2020)
    
    print(carro1.display_details())
   
    
    carro1.accelerate(20)
    carro1.accelerate(30)
    carro1.brake(10)
    print(carro1.display_speed())
    carro1.brake(50)
    print(carro1.display_speed())
