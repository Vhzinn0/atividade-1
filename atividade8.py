class Turma:
    def _init_(self, nome):
        self.nome = nome
        self.estudantes = []


    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
