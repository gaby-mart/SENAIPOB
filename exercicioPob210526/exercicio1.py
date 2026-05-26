class Carro:
    def __init__(self, marca, modelo, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano


carro1 = Carro("Carro 1", "Modelo1", 2020)
carro2 = Carro("Carro 2", "Modelo2", 2020)


def printCarro():
    print(f"Modelo: {carro1.modelo}, Marca: {carro1.marca}, Ano: {carro1.ano}.")
    print(f"Modelo: {carro2.modelo}, Marca: {carro2.marca}, Ano: {carro2.ano}.")



