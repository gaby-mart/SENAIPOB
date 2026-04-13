inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

if inicio < fim:
    primos = []

    for i in range(inicio, fim + 1):

        if i < 2:
            continue

        primo = True

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                primo = False
                break

        if primo:
            primos.append(i)

    print("Primos:", primos)
    print("Quantidade:", len(primos))

else:
    print("Erro: início deve ser menor que fim")



