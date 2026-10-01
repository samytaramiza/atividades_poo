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
"""
# Questão 8


# Questão 9