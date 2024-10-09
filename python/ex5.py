

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def sound(self):
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses")


class Dog(Animal):
    def sound(self):
        return f"{self.nome} faz: Au Au!"


class Cat(Animal):
    def sound(self):
        return f"{self.nome} faz: Miau!"

def make_animals_make_sounds(lista_animais):
    for animal in lista_animais:
        print(animal.sound())


def main():
    cachorro = Dog("Rex")
    gato = Cat("Mimi")
    outro_cachorro = Dog("Bolt")

    
    lista_animais = [cachorro, gato, outro_cachorro]

    
    make_animals_make_sounds(lista_animais)


if __name__ == "__main__":
    main()
