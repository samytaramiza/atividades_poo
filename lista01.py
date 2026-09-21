#QUESTÃO 1
class Aluno:
    def __init__(self, nome:str, matricula:str):
        self.nome = nome
        self.matricula = matricula
        self.notas: list[float]=[]

    def lancar_notas(self, valor:float):
        self.notas.append(valor)

    def media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprovado(self) -> bool:
        return self.media() >= 6

    def str(self):
        return f"{self.nome} ({self.matricula}) - media {self.media():.1f}"