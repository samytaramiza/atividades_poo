# Questão 6
"""class SalarioInvalidoError(Exception): pass
class PercentualInvalidoError(Exception): pass

class Funcionario:
    salario_minimo = 1621

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < self.salario_minimo:
            raise SalarioInvalidoError("Salário inválido. Deve ser maior ou igual ao salário mínimo (1.621,00).")
        self._salario = valor

    def aumentar(self, percentual):
        if percentual <= 0 or percentual > 30:
            raise PercentualInvalidoError("Percentual inválido. Deve ser maior que 0 e menor ou igual a 30.")

        self._salario += self._salario * percentual / 100


funcionario1 = Funcionario("João", 2000)
funcionario1.aumentar(20)
print(f"Salário de {funcionario1.nome}: {funcionario1.salario}")

funcionario2 = Funcionario("Maria", 2500)
print(f"Salário de {funcionario2.nome}: {funcionario2.salario}")
funcionario2.aumentar(10)

# Questão 7
class EmailInvalidoError(Exception): pass

class Email:
    def __init__(self, endereco):
        self.endereco = endereco

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError("Endereço de e-mail inválido.")
        self._endereco = valor

email1 = Email("joao@email.com")
email1.endereco = "joao@email.com"
print(email1.endereco)

email2 = Email("maria@email.com")
print(email2.endereco)
print(email2.endereco)

# Questão 8
try:
    funcionario = Funcionario("João", 1500)
except SalarioInvalidoError as erro:
    print(erro)


funcionario = Funcionario("João", 2000)

try:
    funcionario.aumentar(40)
except PercentualInvalidoError as erro:
    print(erro)


# Teste 3 - e-mail inválido
try:
    email = Email("teste.com")
except EmailInvalidoError as erro:
    print(erro)


try:
    email = Email("testegmail.com")
except EmailInvalidoError as erro:
    print(erro)
"""
# Questão 9
class ErroDeConta(Exception): pass
class ValorInvalidoError(ErroDeConta): pass
class SaldoInsuficienteError(ErroDeConta): pass
class LimiteExcedidoError(ErroDeConta): pass

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("Valor de depósito inválido.")
        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("Valor de saque inválido.")

        if valor > 1000:
            raise LimiteExcedidoError(
                "O limite de saque por operação é R$ 1.000."
            )

        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")

        self._saldo -= valor

conta = ContaBancaria("João")

try:
    conta.depositar(500)
    print(f"Saldo: R$ {conta.saldo:.2f}")

    conta.sacar(200)
    print(f"Saldo: R$ {conta.saldo:.2f}")

    conta.sacar(2000)

except ValorInvalidoError as erro:
    print(erro)

except SaldoInsuficienteError as erro:
    print(erro)

except LimiteExcedidoError as erro:
    print(erro)
    
# Questão 10
conta = ContaBancaria("João")

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Sair")

    try:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Valor do depósito: "))
            conta.depositar(valor)
            print("Depósito realizado com sucesso.")

        elif opcao == "2":
            valor = float(input("Valor do saque: "))
            conta.sacar(valor)
            print("Saque realizado com sucesso.")

        elif opcao == "3":
            print(f"Saldo: R$ {conta.saldo:.2f}")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

    except ValorInvalidoError as erro:
        print(f"Erro: {erro}")

    except SaldoInsuficienteError as erro:
        print(f"Erro: {erro}")

    except LimiteExcedidoError as erro:
        print(f"Erro: {erro}")

    except ValueError:
        print("Digite um valor válido.")