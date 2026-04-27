loginCorreto = "admin"
senhaCorreta = "1234"
i = 3
codProdutos  = []
nomeProdutos = []
precoProdutos = []
qtdProdutos = []
historico_produto = []
historico_qtd = []
historico_valor = []

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
        try:
            qtdCadastros = int(input("Quantos produtos deseja cadastrar?"))
        except ValueError:
            print("Digite um número válido de cadastros.")
        for j in range(qtdCadastros):
            try:
                codProduto = int(input("Digite o codigo do produto: "))
                if codProduto  not in codProdutos:
                    codProdutos.append(codProduto)
                    nomeProduto = str(input("Digite o nome do produto: "))
                    nomeProdutos.append(nomeProduto)
                    precoProduto = float(input("Digite o valor do produto: R$"))
                    precoProdutos.append(precoProduto)
                    qtdProduto = int(input("Quantos produtos tem no estoque:"))

                    if qtdProduto < 0:
                        print("O produto não está disponivel em estoque.")
                    else:
                        qtdProdutos.append(qtdProduto)
                else:
                    print("Produto já cadastrado anteriormente.")
                    break
            except ValueError:
                print("Dados Inválidos, digite novamente.")
    elif escolha == 2:
        if not codProdutos:
            print("Nenhum produto foi cadastrado no sistema.")
        else:
            print("/n" + "="*60)
            print(f"{'Código':<10} | {'Nome':<20} | {'Preço':<12} | {'Estoque':<10}")
            print("-" * 60)

            for cod, nome, preco, qtd in zip(codProdutos, nomeProdutos, precoProdutos, qtdProdutos):
                print(f"{cod:<10} | {nome:<20} | {preco:<12} | {qtd:<10}")

                print("="*60 + '/n')
    elif escolha == 3:
        if not codProdutos:
            print("Nenhum produto foi cadastrado no sistema.")
        else:
            try:
                encontrarProduto = int(input("Digite o codigo do produto: "))

                if encontrarProduto not in codProdutos:
                    print("Produto não cadastrado no sistema.")
                else:
                    indice = codProdutos.index(encontrarProduto)
                    print(f"Código: {codProdutos[indice]} tem {qtdProdutos[indice]} produtos em estoque.")

                    while True:
                        print("1 - Adicionar Produto")
                        print("2 - Remover Produtos")
                        print("3 - Voltar ao menu principal")

                        menu3 = int(input("Digite a opção desejada:"))
                        if menu3 == 1:
                            quantidade = int(input("Qual a quantidade do produto a ser ADICIONADA: "))
                            if quantidade > 0:
                                qtdProdutos[indice] += quantidade
                                print("Estoque atualizado, produto adicionado com sucesso.!")
                            else:
                                print("Quantidade Inválida!")
                        elif menu3 == 2:
                            quantidadeNegativa = int(input("Qual a quantidade do produto deseja Remover: "))
                            if quantidadeNegativa > 0:
                                qtdProdutos[indice] -= quantidadeNegativa
                                print("Estoque atualizado, produto removido com sucesso!")

                                if qtdProdutos[indice] == 0:
                                    print(f"{nomeProdutos[indice]} não está mais em estoque... Removendo do sistema...")
                                    codProdutos.pop(indice)
                                    nomeProdutos.pop(indice)
                                    precoProdutos.pop(indice)
                                    qtdProdutos.pop(indice)
                        elif menu3 == 3:
                            print("Você será direcionado ao menu principal.")
                            break

            except ValueError:
                print("Entrada inválida! Digite apenas valores numéricos.")

    elif escolha == 4:
            encontrarVenda = int(input("Digite o codigo do produto: "))

            if encontrarVenda not in codProdutos:
                print("Produto não disponível no sistema.")
            else:
                    indiceVenda = codProdutos.index(encontrarVenda)

                    try:
                        qtdVendida = int(input("Qual a quantidade do produto desejado: "))

                        if qtdVendida > qtdProdutos[indiceVenda]:
                            print("Produto insuficiente em estoque.")
                            print(f"{nomeProdutos[indiceVenda]} tem {qtdProdutos[indiceVenda]} produtos em estoque.")
                        else:
                            historico_qtd.append(qtdVendida)
                            historico_produto.append(qtdProdutos[indiceVenda])

                            valorTotal = qtdVendida * precoProdutos[indiceVenda]
                            print(f"O valor total da venda é R${valorTotal}")
                            historico_valor.append(valorTotal)

                            if qtdVendida == qtdProdutos[indiceVenda]:
                                print(f"{nomeProdutos[indiceVenda]} não está mais em estoque... Removendo do sistema...")
                                codProdutos.pop(indiceVenda)
                                nomeProdutos.pop(indiceVenda)
                                precoProdutos.pop(indiceVenda)
                                qtdProdutos.pop(indiceVenda)
                    except ValueError:
                        print("Quantidade Inválida! Insira apenas numeros inteiros.")
    elif escolha == 5:
        while True:
            print("1 - Total Vendido")
            print("2 - Produto Mais Vendido")
            print("3 - Produto Com Maior Estoque")
            print("4 - Listar Vendas")
            print("5 - Voltar ao Menu Principal")

            try:
                menu5 = int(input("Digite uma das opções acima:"))
            except ValueError:
                print("Opção Inválida!")

            if menu5 == 1:
                valorVendido = sum(historico_qtd)
                print("O valor total atual de vendas é:R$", valorVendido)
            elif menu5 == 2:
                encontrarMaisVendido = max(historico_qtd)
                indiceMaisVendido = historico_qtd.index(encontrarMaisVendido)

                print(f"O produto mais vendido é: {historico_produto[indiceMaisVendido]} com {historico_qtd[indiceMaisVendido]} quantidade de vendas.")
            elif menu5 == 3:
                encontrarMaiorEstoque = max(qtdProdutos)
                indiceMaiorEstoque = qtdProdutos.index(encontrarMaiorEstoque)

                print(f"O produto com maior estoque é {nomeProdutos[indiceMaiorEstoque]} com {qtdProdutos[indiceMaiorEstoque]} unidades em estoque.")
            elif menu5 == 4:
                if not historico_produto:
                    print("Nenhum produto foi vendido.")
                else:
                    print("/n" + "=" * 60)
                    print(f"{'Código':<10} | {'Nome':<20} | {'Preço':<12} | {'Estoque':<10}")
                    print("-" * 60)

                    for codVenda, precoVenda, qtdVenda in zip(historico_produto, historico_qtd, historico_valor):
                        print(f"{codVenda:<10} | {precoVenda:<12} | {qtdVenda:<10}")
            elif menu5 == 5:
                print("Voltar ao Menu Principal")
                break
