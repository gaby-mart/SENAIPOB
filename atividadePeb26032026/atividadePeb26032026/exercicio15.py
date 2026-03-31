regiao = input("Escreva sua região (Sudestre, Nordeste/Norte, Sul e Centro-Oete:")
peso = float(input("Escreva o peso do pacote:"))

status = int(input("Escreva a status do cliente (Padrão/Premium):"))

if status == "Padrão":
    if regiao == "Sudeste":
        valorTota = 10 + peso * 2
        print(f'O valor total é {valorTota}')
    elif regiao == "Sul":
        valorTota = 15 + peso * 3
        print(f'O valor total é: {valorTota}')
    elif regiao == "Nordeste/Norte":
        valorTota = 25 + peso * 5
        print(f'O valor total é: {valorTota}')
    elif regiao == "Centro-Oete":
        valorTota = 20 + peso * 4
        print(f'O valor total é: {valorTota}')
    else:
        print("Região invalida")
else:
    if regiao == "Sudeste":
        valorTota = 10 + peso * 2
        valorDesconto = valorTota - valorTota * 0.2
        print(f'O valor total é {valorTota}')
    elif regiao == "Sul":
        valorTota = 15 + peso * 3
        valorDesconto = valorTota - valorTota * 0.
        print(f'O valor total é: {valorTota}')
    elif regiao == "Nordeste/Norte":
        valorTota = 25 + peso * 5
        valorDesconto = valorTota - valorTota * 0.
        print(f'O valor total é: {valorTota}')
    elif regiao == "Centro-Oete":
        valorTota = 20 + peso * 4
        valorDesconto = valorTota - valorTota * 0.
        print(f'O valor total é: {valorTota}')
    else:
        print
