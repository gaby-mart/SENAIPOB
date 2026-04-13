num = 0

while True:
    num = input("Digite um número (ou 'sair' para encerrar):")

    if num.lower() == "sair":
        print("Saindo do sistema...")
        break

    numero = int(num)
    fatorial = 1

    for i in range (1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")