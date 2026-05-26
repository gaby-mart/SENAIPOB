class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

produto1 = Produto("Socorro", 100, 10)
produto2 = Produto("Socorro2", 1200, 120)

def mostraEstoque():
    print(f"Nome do produto: {produto1.nome}")
    print(f"Preço do produto: {produto1.preco}")
    print(f"Quantidade de produtos: {produto1.qtd}")

mostraEstoque()