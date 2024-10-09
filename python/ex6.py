

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def display_power(self):
        return f"Potência do motor: {self.potencia} CV"

class Car:
    def __init__(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor  

    def display_details(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, "
                f"{self.motor.display_power()}")


def main():
    motor_v8 = Motor(450)  
    carro1 = Car("Ford", "Mustang", 2022, motor_v8)  

    
    print(carro1.display_details())


if __name__ == "__main__":
    main()

