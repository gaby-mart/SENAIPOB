from exercicio1 import Carro, printCarro
from exercicio2 import Pessoa, printPessoa
from exercicio3 import Manuais, pesquisarManual
from exercicio4 import Produto, mostraEstoque
from exercicio5 import Treinamento, descricao
from exercicio6 import Aluno, status

carro1 = Carro("Carro 1", "Modelo1", 2020)
carro2 = Carro("Carro 2", "Modelo2", 2020)

pessoa1 = Pessoa("Julia", 20, "M")
pessoa2 = Pessoa("Michel", 20, "M")

manual1 = Manuais("Plantadeira", "Esqueci o nome", "2020")
manual2 = Manuais("Furadeira", "blablabla", "2023")

produto1 = Produto("Socorro", 100, 10)
produto2 = Produto("Socorro2", 1200, 120)

treinamento1 = Treinamento("AAAAAAAAAAA", "BBBBBB", "12")
treinamento2 = Treinamento("AAAAAAABAAAA", "BBBBBB", "12")

aluno1 = Aluno("Socorro", "Curso de um aluno", 1)
aluno2 = Aluno("Socorro2", "Curso de um aluno", 2)

while True:
    print("\n------MENU-------")
    print("1 - Visualizar Carros")
    print("2 - Visualizar Pessoas")
    print("3 - Visualizar Manuais")
    print("4 - Visualizar Produtos")
    print("5 - Visualizar Treinamentos")
    print("6 - Mostrar Alunos")
    print("7 - Sair")

    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            printCarro(carro1, carro2)
        elif opcao == 2:
            printPessoa(pessoa1, pessoa2)
        elif opcao == 3:
            pesquisarManual(manual1, manual2)
        elif opcao == 4:
            mostraEstoque(produto1, produto2)
        elif opcao == 5:
            descricao(treinamento1, treinamento2)
        elif opcao == 6:
            status(aluno1, aluno2)
        elif opcao == 7:
            print("Fechando o programa.....")
            break
        else:
            print("Opção Inválida!")

    except ValueError:
        print("Por favor, insira apenas números inteiros.")


