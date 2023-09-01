class Computador:
    def _init_(self,sistema):
        self.sistema = sistema


    def mostrar_info(self):
        return f"Computador com{self.sistema.mostrar_info()}"