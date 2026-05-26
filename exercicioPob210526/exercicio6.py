class Aluno:
    def __init__(self, nome, curso, nota):
        self.nome = nome
        self.curso = curso
        self.nota = nota

aluno1 = Aluno("Socorro", "Curso de um aluno", 1)
aluno2 = Aluno("Socorro2", "Curso de um aluno", 2)

def status():
    print(f"O aluno {aluno1.nome}, do curso de {aluno1.curso}, teve a média final de {aluno1.nota}")

status()