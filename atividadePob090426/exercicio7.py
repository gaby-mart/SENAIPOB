matriz = []
soma = 0
maior = None
somaDiagonal = 0
pares = 0

for i in range (1, 4):
    linha = []
    for j in range (1, 4):
        num = int(input(f"Digite um número para a posição [{i}] e [{j}]:"))
        linha.append(num)

        soma += num

        if maior is None or num> maior:
            maior = num

        if i == j:
            somaDiagonal += num

        if num % 2 == 0:
            pares += 1

    matriz.append(linha)

print("\nMatriz:")
for linha in matriz:
    print(linha)

print("\nSoma total:", soma)
print("Maior valor:", maior)
print("Soma da diagonal principal:", somaDiagonal)
print("Quantidade de números pares:", pares)
