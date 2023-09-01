class Endereco:
    def _init_(self,rua,cidade):
        self.rua = rua
        self.cidade = cidade
 
    def monstra_endereco(self):
        return f"(self.rua),(self.cidade)"
       