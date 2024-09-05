from enum import Enum
import os

os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Aluno :
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome 
        self.idade = idade 
        self.sexo = sexo 

    def __str__(self) -> str:
       return  (f"Nome: {self.nome}\n"
                f"Idade: {self.idade}\n"
                f"Sexo: {self.sexo.value}"     
       )

aluno1 = Aluno("Rafael", 23, Sexo.MASCULINO)

print(aluno1)
