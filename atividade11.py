import os


class Pessoa:
    def _init_(self,nome,sobrenome):
        os.system("class")
        self.nome = nome
        self.sobrenome = sobrenome




    def mostrar_dados(self):
        print(self.nome, self.sobrenome)