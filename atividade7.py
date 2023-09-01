class Carro:
    def _init_(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor


motor_do_carro = motor(gasolina=True, diesel=False, eletrico=True, potencia=150)
carro = Carro(marca="Toyota", modelo="Corolla", ano=2023, motor=motor_do_carro)


print(f"Carro: {carro.marca} {carro.modelo} {carro.ano}")
print("Tipo de Motor:")
print(f"Gasolina: {carro.motor.gasolina}")
print(f"Diesel: {carro.motor.diesel}")
print(f"Elétrico: {carro.motor.eletrico}")
print(f"Potência: {carro.motor.potencia} cavalos")
