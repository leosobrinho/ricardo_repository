

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def sound(self):
        raise NotImplementedError("Método deve ser sobrescrito pelas subclasses")


class Dog(Animal):
    def sound(self):
        return f"{self.nome} faz: Au Au!"


class Cat(Animal):
    def sound(self):
        return f"{self.nome} faz: Miau!"


def main():
    dog = Dog("Tobby")
    cat = Cat("Luana")

    
    print(dog.sound())
    print(cat.sound())


if __name__ == "__main__":
    main()
