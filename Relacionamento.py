import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str )-> None:
        self.logradouro = logradouro       
        self.numero = numero       

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}\n" 
                f"Número: {self.numero}"
                )


class Aluno: 
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome 
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"Nome: {self.nome}\n" 
                f"Idade: {self.idade}\n"
                f"=== Endereço === {self.endereco}"
                )

    
endereco1 = Endereco("Rua ...", "644")    
aluno1 = Aluno("Rafael", 22, endereco1)

print(aluno1)
