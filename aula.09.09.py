R=1
class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

R=2
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Alice", 18)

print(f"Pessia 1: Nome - {pessoa1.nome}, Idade - {pessoa1.idade}")
print(f"Pessia 2: Nome - {pessoa2.nome}, Idade - {pessoa2.idade}")

class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
            print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa3 = Pessoa ("joão", 40)
pessoa3.apresentar()

R=3
class Carro:
    def __init__(self, marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("renault", "sandero", "2018")
carro2 = Carro("volkswagen", "fox", "2013")
carro3 = Carro("fiat", "touro", "2025")

print(f"carro 1: marca - {carro1.marca}, modelo - {carro1.modelo}, ano - {carro1.ano}")
print(f"carro 2: marca - {carro2.marca}, modelo - {carro2.modelo}, ano - {carro2.ano}")
print(f"carro 3: marca - {carro3.marca}, modelo - {carro3.modelo}, ano - {carro3.ano}")

R=4
Carro_teste = Carro("fiat", "touro",2025)
print(f"ano do carro antes da alteração:{Carro_teste.ano}")
Carro_teste.ano = 2023
print(f"ano do carro depois da alteração:{Carro_teste.ano}")

R=5
class ContaBancaria: 
    def __init__(self, numero, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("saque se {valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente para saque.")

conta1 = ContaBancaria("1759-3", "Angela Souza", 1000)
conta1.depositar(500)
conta1.sacar(200)
conta1.sacar(2000) # Tentativa de saque com saldo insuficiente

R=6
class ContaBancaria: 
    def __init__(self, numero, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
       else:
            return False
