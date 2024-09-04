from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}\n" 
                f"Número: {self.numero}\n"
                f"Complemento: {self.complemento}\n"
                f"CEP: {self.cep}\n"
                f"Cidade: {self.cidade}\n"
                )
        

class Funcionario(ABC): 
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"E-mail: {self.email}\n"
                f"=== Endereço === {self.endereco}"
                f"Salario: {self.salario}\n"
                f"Salario Final: {self.salario_final():.2f}"
                )

class Engenheiro(Funcionario): 
    BONIFICACAO = 1.1
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario)
        self.crea = crea

    def salario_final(self) -> float:
        resultado =  self.salario * self.BONIFICACAO
        return resultado
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
        )


class Medico(Funcionario):
    BONIFICACAO = 1.25
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, salario)
        self.crm = crm
        
    def salario_final(self) -> float:
        resultado =  self.salario * self.BONIFICACAO
        return resultado   
     
    def __str__(self) -> str:
        return (f"{super().__str__()}"
        f"\nCRM: {self.crm}"
        )
    
endereco1 = Endereco("Rua ...", "6666", "Apto 202", "41200500", "Salvador")
endereco2 = Endereco("Avenida ...", "7777", "Apto 304", "42800750", "Feira de Santana")
engenheiro1 = Engenheiro("João", "7198888", "João@....", endereco2, 1800, "5555")
medico1 = Medico("Lucas", "71999999", "Lucas@....", endereco1, 1800, "4444")

print(engenheiro1)
print("\n")
print(medico1)