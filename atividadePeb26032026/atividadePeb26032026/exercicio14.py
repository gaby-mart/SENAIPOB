numero = int(input("Digite um número inteiro de ezatamente 5 digidos:"))

if len(numero) != 5:
    print("Número inválido.")
else:
    a = numero // 10000
    b = (numero // 1000) % 10
    c = (numero // 10) % 10
    d = numero % 10

    if a == d and b == d:
        print("É um palindromo")
    else:
        print("Não é um palindromo")