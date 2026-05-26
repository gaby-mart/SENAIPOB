class Manuais:
    def __init__(self, nome, autor, ano):
        self.nome = nome
        self.autor = autor
        self.ano = ano

manual1 = Manuais("Plantadeira", "Esqueci o nome", "2020")
manual2 = Manuais("Furadeira", "blablabla", "2023")

def pesquisarManual():
    pesquisa = str(input("Digite o nome do Manual: "))

    if pesquisa == manual1.nome:
        print(f"O manual {manual1.nome}, escrito por {manual1.autor}, foi publicado em {manual1.ano}")
    elif pesquisa == manual2.nome:
        print(f"O manual {manual2.nome}, escrito por {manual2.autor}, foi publicado em {manual2.ano}")
    else:
        print("Manual não encontrado")

pesquisarManual()


