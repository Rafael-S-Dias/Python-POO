import os

os.system("cls || clear")

class Aluno: 
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome 
        self.idade = idade 

    def exibir_dados(self) -> str:
        return (f"Nome: {self.nome}\n" 
                f"Idade: {self.idade}"
                )

aluno = Aluno("Rafael", 22)

print(aluno.exibir_dados())