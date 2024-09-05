from enum import Enum
import os

os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario :
    def __init__(self, id: str, nome: str, salario: float, sexo: Sexo, setor: Setor, idade: int) -> None:
        self.id = id 
        self.nome = nome 
        self.salario = salario 
        self.sexo = sexo 
        self.setor = setor 
        self.idade = idade 

    def __str__(self) -> str:
       return  (f"id: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Salario: {self.salario}\n"     
                f"Setor: {self.setor.value}\n"     
                f"Sexo: {self.sexo.value}\n"     
                f"Idade: {self.idade}\n"
       )

funcionario1 = Funcionario("888","Rafael", 2500, Setor.FINANCEIRO, 23)

print(funcionario1)
