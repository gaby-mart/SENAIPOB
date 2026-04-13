import time

N = int(input("Digite um número N: "))

inicio = time.time()

# cria lista (True = primo)
primo = [True] * (N + 1)
primo[0] = primo[1] = False

for i in range(2, int(N**0.5) + 1):
    if primo[i]:
        for j in range(i * i, N + 1, i):
            primo[j] = False

# lista de primos
listaPrimos = []
for i in range(2, N + 1):
    if primo[i]:
        listaPrimos.append(i)

fim = time.time()

# resultados
print("\nNúmeros primos:")
print(listaPrimos)

print("\nQuantidade:", len(listaPrimos))
print("Tempo de execução:", fim - inicio, "segundos")

