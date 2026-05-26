class Treinamento():
    def __init__(self, titulo, instrutor, duracao):
       self.titulo = titulo
       self.instrutor = instrutor
       self.duracao = duracao

treinamento1 = Treinamento("AAAAAAAAAAA", "BBBBBB", "12")
treinamento2 = Treinamento("AAAAAAABAAAA", "BBBBBB", "12")

def descricao():
    print(f"Treinamento: {treinamento1.titulo}, é lecionado por {treinamento1.instrutor}, durante {treinamento1.duracao} meses")

descricao()