colunaInicial = int(input("Digite a coluna:"))
linhaInicial = int(input("Digite a linha:"))
colunaFinal = int(input("Digite a coluna de destino:"))
linhaFinal = int(input("Digite a linha de destino:"))

if colunaInicial > 8 or linhaInicial > 8 or colunaFinal > 8 or linhaFinal > 8:
    print("Posição Inválida")
else:
    if colunaInicial - linhaFinal == 3 or colunaInicial - linhaFinal == -3:
        if linhaInicial - colunaFinal == 1 or colunaInicial == -1:
            print("Movimento válido em L.")
        else:
            print("Movimento Inválido.")
    else:
        print("Movimento Inválido.")