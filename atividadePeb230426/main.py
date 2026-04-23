loginCorreto = "admin"
senhaCorreta = "1234"
i = 3

while i > 0:
    tentativaLogin = input("Digite o login: ")
    tentativaSenha = input("Digite a senha: ")

    if tentativaLogin != loginCorreto and tentativaSenha != senhaCorreta:
        print("Login incorreto")
        i -= 1
        if i > 0:
            print(f"Você tem {i} tentativas restantes.")
        else:
            print("Sistema Bloqueado, número de tentativas máximas superado.")
            break
    else:
        print("Seja Bem-Vindo ADM")
        break

while True:
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar Estoque")
    print("4 - Realizar Venda")
    print("5 - Relatório")
    print("6 - Sair")

    escolha = int(input("Escolha uma opção do menu acima:"))

    if escolha == 1:


