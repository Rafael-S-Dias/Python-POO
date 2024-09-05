import os

os.system("cls || clear")

class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class Conta: 
    def __init__(self, numero_conta: int, agencia: str) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 10

    def __str__(self) -> str:
        return (f"Número da Conta: {self.numero_conta}\n"
                f"Agencia: {self.agencia}\n"
                f"Saldo: {self._saldo}"
        )

    @property
    def saldo(self):
        return self._saldo

    def __verificar_sacar(self, valor) -> None:
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente!")

        if valor < 0:
            raise ValorNegativoError("Valor negativo inserido!")
        

    def sacar(self) -> str:
        valor_saque = float(input("Digite o valor do saque: "))

        try:
            self.__verificar_sacar(valor_saque)
        except (SaldoInsuficienteError, ValorNegativoError) as erro:
            return f"Erro: {erro}"

        self._saldo -= valor_saque
        return f"Saldo Realizado com Sucesso"
        
    
    def depositar(self, valor) :
        self._saldo += valor
        return self._saldo   


class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

conta1 = ContaCorrente(444, "02")

print(conta1.sacar())
print(conta1)
