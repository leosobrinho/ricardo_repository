

class BankAccount:
    def __init__(self, titular, saldo_inicial=0):
        self.__saldo = saldo_inicial  
        self.titular = titular

    #
    def deposit(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    
    def withdraw(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor de saque deve ser positivo.")

    
    def display_balance(self):
        return f"Saldo atual: R${self.__saldo:.2f}"


def main():
    conta = BankAccount("Leonardo Sobrinho", 1000)
    
    
    print(conta.display_balance())
    
    
    conta.deposit(500)
    print(conta.display_balance())
    
    conta.withdraw(300)
    print(conta.display_balance())
    
    conta.withdraw(1500)  


if __name__ == "__main__":
    main()
