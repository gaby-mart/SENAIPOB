funcaoMenu = ["Depositar", "Sacar", "Ver saldo", "Sair"]
saldo = 1000

while True:
    print("\nMenu:")
    print("a - Depositar")
    print("b - Sacar")
    print("c - Ver saldo")
    print("d - Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "a":
        valor = float(input("Valor do depósito: "))
        saldo += valor
        print("Saldo: ", saldo)

    elif opcao == "b":
        valor = float(input("Valor do saque: "))
        saldo -= valor
        print("Saldo: ", saldo)

    elif opcao == "c":
        print(f"Saldo: {saldo:.2f}")

    elif opcao == "d":
        print("Desligamento do Sistema.")
        break
    else:
        print("Opção inválida!")