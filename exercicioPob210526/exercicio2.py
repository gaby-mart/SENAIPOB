class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

pessoa1 = Pessoa("Julia", 20, "M")
pessoa2 = Pessoa("Michel", 20, "M")

def printPessoa():
    print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Setor: {pessoa1.setor}.")
    print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}, Setor: {pessoa2.setor}.")