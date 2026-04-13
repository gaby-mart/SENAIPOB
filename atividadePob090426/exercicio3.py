senha = "socorro"
i = 1

while i <= 3:
    tentativa = str(input("Digte a senha:"))
    if tentativa != senha:
        print("Senha incorreta")
        print(f'Você usou {i} tentativas')
        i = i + 1
    else:
        print("Senha correta")
        print(f'Você usou {i} tentativas')
        break