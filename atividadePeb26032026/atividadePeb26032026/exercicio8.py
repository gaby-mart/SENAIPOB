valor = int(input("Digite o valor para saque: "))

if valor <= 0:
    print("Valor inválido")
else:
    notas = [100, 50, 20, 10, 5, 2]
    resto = valor

    for nota in notas:
        qtd = resto // nota
        resto = resto % nota

        if qtd > 0:
            print(f"{qtd} nota(s) de R${nota}")

    if resto != 0:
        print("Valor impossível de sacar com as notas disponíveis.")